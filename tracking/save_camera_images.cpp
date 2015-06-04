#include "FlyCapture2.h"

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <iostream>

#include <boost/filesystem.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>


static void help()
{
  std::cout
    << "------------------------------------------------------------------------------" << std::endl
    << "This program writes image files from camera."                                   << std::endl
    << "Usage:"                                                                         << std::endl
    << "save-camera-images output_path_base"                                            << std::endl
    << "------------------------------------------------------------------------------" << std::endl
    << std::endl;
}

boost::filesystem::path createDirectory(const boost::filesystem::path &path)
{
  if (!boost::filesystem::exists(path))
  {
    if(boost::filesystem::create_directory(path)) {
      std::cout << "Created directory: " << path << std::endl;
    }
    else
    {
      std::cout << "Unable to create directory: " << path << std::endl;
    }
  }
  else if (boost::filesystem::is_directory(path))
  {
    std::cout << "Directory exists: " << path << std::endl;
  }
  else
  {
    std::cout << "Error! " << path << " exists, but is not a directory!" << std::endl;
  }
  return path;
}

int main(int argc, char *argv[])
{
  help();

  if (argc != 2)
  {
    std::cout << "Not enough parameters" << std::endl;
    return -1;
  }

  // Create base directory
  boost::filesystem::path output_path_base(argv[1]);
  createDirectory(output_path_base);

  // Create directory for saving images
  boost::posix_time::ptime date_time = boost::posix_time::second_clock::local_time();
  std::string date_time_string = boost::posix_time::to_iso_string(date_time);
  boost::filesystem::path output_dir(date_time_string);
  boost::filesystem::path output_path = output_path_base / output_dir;
  createDirectory(output_path);

  // Setup image parameters
  std::vector<int> compression_params;
  compression_params.push_back(CV_IMWRITE_PNG_COMPRESSION);
  compression_params.push_back(0);

  // Connect the camera
  FlyCapture2::Error error;
  FlyCapture2::Camera camera;
  FlyCapture2::CameraInfo camInfo;

  error = camera.Connect( 0 );
  if ( error != FlyCapture2::PGRERROR_OK )
  {
    std::cout << "Failed to connect to camera" << std::endl;
    return false;
  }

  // Get the camera info and print it out
  error = camera.GetCameraInfo( &camInfo );
  if ( error != FlyCapture2::PGRERROR_OK )
  {
    std::cout << "Failed to get camera info from camera" << std::endl;
    return false;
  }
  std::cout << camInfo.vendorName << " "
            << camInfo.modelName << " "
            << camInfo.serialNumber << std::endl;

  error = camera.StartCapture();
  if ( error == FlyCapture2::PGRERROR_ISOCH_BANDWIDTH_EXCEEDED )
  {
    std::cout << "Bandwidth exceeded" << std::endl;
    return false;
  }
  else if ( error != FlyCapture2::PGRERROR_OK )
  {
    std::cout << "Failed to start image capture" << std::endl;
    return false;
  }

  // Capture loop
  char key = 0;
  while(key != 'q')
  {
    // Get the image
    FlyCapture2::Image rawImage;
    FlyCapture2::Error error = camera.RetrieveBuffer( &rawImage );
    if ( error != FlyCapture2::PGRERROR_OK )
    {
      std::cout << "capture error" << std::endl;
      continue;
    }

    // Convert to rgb
    FlyCapture2::Image rgbImage;
    rawImage.Convert( FlyCapture2::PIXEL_FORMAT_BGR, &rgbImage );

    // Convert to OpenCV Mat
    unsigned int rowBytes = (double)rgbImage.GetReceivedDataSize()/(double)rgbImage.GetRows();
    cv::Mat image = cv::Mat(rgbImage.GetRows(), rgbImage.GetCols(), CV_8UC3, rgbImage.GetData(),rowBytes);

    // Show image
    cv::imshow("image", image);
    key = cv::waitKey(30);

    // Create full image output path
    date_time = boost::posix_time::microsec_clock::local_time();
    std::string time_string = boost::posix_time::to_iso_string(date_time);
    std::ostringstream image_file_name;
    image_file_name << time_string << ".png";
    std::string image_file_name_string = image_file_name.str();
    boost::filesystem::path output_file_name_path(image_file_name_string);
    boost::filesystem::path output_path_full = output_path / output_file_name_path;

    // Write image to file
    cv::imwrite(output_path_full.string(),image,compression_params);
  }

  error = camera.StopCapture();
  if ( error != FlyCapture2::PGRERROR_OK )
  {
    // This may fail when the camera was removed, so don't show
    // an error message
  }

  camera.Disconnect();

  return 0;
}
