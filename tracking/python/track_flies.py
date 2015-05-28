#!/usr/bin/env python
from __future__ import print_function,division
import argparse
import os
import cv2
import numpy
import scipy.io
import sys
import time

from diskwalk import DiskWalk

DEBUG = True

class FlyTracker(object):
    def __init__(self):
        self.image_ext = ".pgm"
        # self.video_ext = ".avi"
        # self.trx_filename = "trx.mat"
        # self.features_filename = "features.mat"
        # self.patch_half_size = 200
        # self.norm_radius = 5
        # self.norm_const = 0.005
        # self.triangle_filter_2D = self.get_triangle_filter_2D(self.norm_radius)

    def condition_path(self,path):
        return os.path.normpath(os.path.expanduser(path))

    def get_image_paths(self,directory):
        dw = DiskWalk(directory)
        paths_images_ext = dw.enumerate_paths_with_ext(self.image_ext)
        return paths_images_ext

    # def get_video(self,directory):
    #     dw = DiskWalk(directory)
    #     paths_video_ext = dw.enumerate_paths_with_ext(self.video_ext)
    #     if len(paths_video_ext) == 1:
    #         video_path = paths_video_ext[0]
    #     elif len(paths_video_ext) > 1:
    #         print("Found multiple videos in {0}".format(directory))
    #         sys.exit(1)
    #     else:
    #         print("Cannot find video in {0}".format(directory))
    #         sys.exit(1)
    #     try:
    #         video = cv2.VideoCapture(video_path)
    #     except:
    #         print("Problem opening video {0}".format(video_path))
    #         sys.exit(1)
    #     if not video.isOpened():
    #         print("{0} not opened".format(video_path))
    #         sys.exit(1)
    #     else:
    #         print("Found video {0}".format(video_path))
    #     return video

    # def get_interest_points(self,directory):
    #     trx_path = os.path.join(directory,self.trx_filename)
    #     trx = scipy.io.loadmat(trx_path)
    #     interest_points = []
    #     interest_points_count = len(trx['trx']['x'][0])
    #     for point_index in range(interest_points_count):
    #         x = int(trx['trx']['x'][0][point_index][0][0])
    #         y = int(trx['trx']['y'][0][point_index][0][0])
    #         interest_point = (x,y)
    #         interest_points.append(interest_point)
    #     return interest_points

    # def extract_patches(self,image,interest_points):
    #     image = cv2.cvtColor(image,cv2.cv.CV_BGR2GRAY)
    #     patch_count = len(interest_points)
    #     patch_size = self.patch_half_size*2
    #     if DEBUG:
    #         print("image.shape = {0}".format(image.shape))
    #         print("image.dtype = {0}".format(image.dtype))
    #     if len(image.shape) == 3:
    #         patch_image = numpy.zeros((patch_size,patch_size*patch_count,image.shape[2]),image.dtype)
    #     else:
    #         patch_image = numpy.zeros((patch_size,patch_size*patch_count),image.dtype)
    #     for patch_n in range(patch_count):
    #     # for patch_n in range(1):
    #         px0 = patch_size*patch_n
    #         py0 = 0
    #         px1 = px0 + patch_size
    #         py1 = py0 + patch_size
    #         if DEBUG:
    #             print('patch: {0}'.format(patch_n))
    #             print('px0 = {0}, px1 = {1}, py0 = {2}, py1 = {3}'.format(px0,px1,py0,py1))
    #         interest_point = interest_points[patch_n]
    #         ix0 = interest_point[0] - self.patch_half_size
    #         iy0 = interest_point[1] - self.patch_half_size
    #         ix1 = interest_point[0] + self.patch_half_size
    #         iy1 = interest_point[1] + self.patch_half_size
    #         if DEBUG:
    #             print('ix0 = {0}, ix1 = {1}, iy0 = {2}, iy1 = {3}'.format(ix0,ix1,iy0,iy1))
    #         if ix0 < 0:
    #             px0 = px0 + abs(ix0)
    #             ix0 = 0
    #         if iy0 < 0:
    #             py0 = py0 + abs(iy0)
    #             iy0 = 0
    #         if ix1 > image.shape[1]:
    #             px1 = px1 + (image.shape[1] - ix1)
    #             ix1 = image.shape[1]
    #         if iy1 > image.shape[0]:
    #             py1 = py1 + (image.shape[0] - iy1)
    #             iy1 = image.shape[0]
    #         if DEBUG:
    #             print('px0 = {0}, px1 = {1}, py0 = {2}, py1 = {3}'.format(px0,px1,py0,py1))
    #             print('ix0 = {0}, ix1 = {1}, iy0 = {2}, iy1 = {3}'.format(ix0,ix1,iy0,iy1))
    #             print('')
    #         patch_image[py0:py1,px0:px1] = image[iy0:iy1,ix0:ix1]
    #     return patch_image

    # def annotate_original_image(self,image,interest_points):
    #     image = numpy.copy(image)
    #     for interest_point in interest_points:
    #         cv2.circle(image,interest_point,5,(0,0,255),-1)
    #         point1 = (interest_point[0]-self.patch_half_size,interest_point[1]-self.patch_half_size)
    #         point2 = (interest_point[0]+self.patch_half_size,interest_point[1]+self.patch_half_size)
    #         cv2.rectangle(image,point1,point2,(0,0,255))
    #     return image

    # def show_image(self,image,window_name):
    #     if DEBUG:
    #         cv2.imshow(window_name, image)

    # def save_image(self,image,directory,file_name):
    #     if DEBUG:
    #         image_path = os.path.join(directory,file_name)
    #         cv2.imwrite(image_path,image)

    # def get_triangle_filter_2D(self,radius):
    #     const = (radius+1)**2
    #     f = []
    #     for i in range(radius+1):
    #         f.append((i+1)/const)
    #     for i in range(radius+1,2*radius+1):
    #         f.append((2*radius+1-i)/const)
    #     f_array = numpy.array([f],numpy.float32)
    #     f_array_transpose = numpy.transpose(f_array)
    #     triangle_filter_2D = numpy.dot(f_array_transpose,f_array)
    #     return triangle_filter_2D

# cv::Mat getTriangleFilter1D(unsigned int normRadius)
# {
#   float normConst = std::pow(float(normRadius)+1,2);
#   cv::Mat f = cv::Mat(1,2*normRadius+1,CV_32FC1);

#   for (unsigned int i=0; i<normRadius+1; i++)
#     {
#       f.at<float>(0,i) = float(i+1)/normConst;
#     }
#   for (unsigned int i=normRadius+1; i<2*normRadius+1;i++)
#     {
#       f.at<float>(0,i) = float(2*normRadius+1-i)/normConst;
#     }
#   return f;
# }

# cv::Mat getTriangleFilter2D(unsigned int normRadius)
# {
#   cv::Mat f1D = getTriangleFilter1D(normRadius);
#   cv::Mat f2D = f1D.t()*f1D;
#   return f2D;
# }

    # def get_gradient_data(self,image,directory):
    #     DEBUG = False
    #     method = "GRAD_METHOD_SCHARR"
    #     # method = "GRAD_METHOD_SOBEL"
    #     # scale = 1
    #     # delta = 0

    #     if DEBUG:
    #         # cv2.imshow("test", image)
    #         # cv2.waitKey(500)
    #         print("image.shape = {0}".format(image.shape))
    #         print("max image = {0}".format(numpy.max(image)))
    #         print("min image = {0}".format(numpy.min(image)))
    #     if method == "GRAD_METHOD_SCHARR":
    #         # scale = 1.0/32.0
    #         # dx = cv2.Scharr(image,cv2.CV_32F,1,0,scale,delta,cv2.BORDER_REPLICATE)
    #         # dy = cv2.Scharr(image,cv2.CV_32F,0,1,scale,delta,cv2.BORDER_REPLICATE)
    #         dx = cv2.Scharr(image,cv2.CV_32F,1,0)
    #         dy = cv2.Scharr(image,cv2.CV_32F,0,1)
    #         print("dx.shape = {0}, dy.shape= {1}".format(dx.shape,dy.shape))
    #     # else:
    #     #     ksize = 5
    #     #     # scale = 1.0/8.0
    #     #     dx = cv2.Sobel(image,cv2.CV_32F,1,0,ksize,scale,delta,cv2.BORDER_REPLICATE)
    #     #     dy = cv2.Sobel(image,cv2.CV_32F,0,1,ksize,scale,delta,cv2.BORDER_REPLICATE)
    #     if DEBUG:
    #         dx_scale_abs = cv2.convertScaleAbs(dx)
    #         cv2.imshow("dx_scale_abs", dx_scale_abs)
    #         im_path = os.path.join(directory,"dx.png")
    #         cv2.imwrite(im_path,dx_scale_abs)
    #         dy_scale_abs = cv2.convertScaleAbs(dy)
    #         cv2.imshow("dy_scale_abs", dy_scale_abs)
    #         im_path = os.path.join(directory,"dy.png")
    #         cv2.imwrite(im_path,dy_scale_abs)
    #         cv2.waitKey(5000)
    #         print("dx dtype = {0}".format(dx.dtype))
    #         print("dx max = {0}".format(numpy.max(dx)))
    #         print("dx min = {0}".format(numpy.min(dx)))
    #         print("dy max = {0}".format(numpy.max(dy)))
    #         print("dy min = {0}".format(numpy.min(dy)))
    #     mag,angle = cv2.cartToPolar(dx,dy)
    #     DEBUG = False
    #     if DEBUG:
    #         print("mag dtype = {0}".format(mag.dtype))
    #         print("mag max = {0}".format(numpy.max(mag)))
    #         print("mag min = {0}".format(numpy.min(mag)))
    #         print("angle max = {0}".format(numpy.max(angle)))
    #         print("angle min = {0}".format(numpy.min(angle)))
    #     angle = numpy.mod(angle,numpy.pi)
    #     if DEBUG:
    #         print("angle max = {0}".format(numpy.max(angle)))
    #         print("angle min = {0}".format(numpy.min(angle)))
    #         mag_scale_abs = cv2.convertScaleAbs(mag)
    #         cv2.imshow("mag_scale_abs", mag_scale_abs)
    #         im_path = os.path.join(directory,"mag.png")
    #         cv2.imwrite(im_path,mag_scale_abs)
    #         angle_norm = angle*(255/numpy.max(angle))
    #         angle_scale_abs = cv2.convertScaleAbs(angle_norm)
    #         cv2.imshow("angle_scale_abs", angle_scale_abs)
    #         im_path = os.path.join(directory,"angle.png")
    #         cv2.imwrite(im_path,angle_scale_abs)
    #         cv2.waitKey(15000)
    #     if self.norm_radius == 0:
    #         mag_smooth = mag
    #     else:
    #         mag_smooth = cv2.filter2D(mag,-1,self.triangle_filter_2D)
    #         mag_norm = mag/(mag_smooth + self.norm_const)
    #     if DEBUG:
    #         print("mag_smooth dtype = {0}".format(mag_smooth.dtype))
    #         print("mag_smooth max = {0}".format(numpy.max(mag_smooth)))
    #         print("mag_smooth min = {0}".format(numpy.min(mag_smooth)))
    #         mag_smooth_scale_abs = cv2.convertScaleAbs(mag_smooth)
    #         cv2.imshow("mag_smooth_scale_abs", mag_smooth_scale_abs)
    #         im_path = os.path.join(directory,"mag_smooth.png")
    #         cv2.imwrite(im_path,mag_smooth_scale_abs)
    #         cv2.waitKey(15000)
    #     DEBUG = True
    #     if DEBUG:
    #         print("mag_norm dtype = {0}".format(mag_norm.dtype))
    #         print("mag_norm max = {0}".format(numpy.max(mag_norm)))
    #         print("mag_norm min = {0}".format(numpy.min(mag_norm)))
    #         mag_norm_scale = mag_norm*(255/numpy.max(mag_norm))
    #         mag_norm_scale_abs = cv2.convertScaleAbs(mag_norm_scale)
    #         cv2.imshow("mag_norm_scale_abs", mag_norm_scale_abs)
    #         im_path = os.path.join(directory,"mag_norm.png")
    #         cv2.imwrite(im_path,mag_norm_scale_abs)
    #         cv2.waitKey(15000)

      # cv::Mat triFilter = getTriangleFilter2D(normRadius);
      # cv::filter2D(
      #              gradData.mag,
      #              smoothMag,
      #              -1,
      #              triFilter,
      #              cv::Point(-1,-1),
      #              0.0,
      #              cv::BORDER_REPLICATE
      #              );

    def process_images(self,directory):
        directory = self.condition_path(directory)
        image_paths = self.get_image_paths(directory)
        # cv2.namedWindow("Original")
        # cv2.namedWindow("Background")
        # cv2.namedWindow("Foreground")
        # cv2.namedWindow("Threshold")
        # cv2.namedWindow("Morphed")
        cv2.namedWindow("Color")
        image = cv2.imread(image_paths[0],cv2.CV_LOAD_IMAGE_GRAYSCALE)
        image_avg = numpy.float32(image)
        background = cv2.convertScaleAbs(image_avg)
        video_writer = cv2.VideoWriter()
        # fps = 15
        # video_writer.open("out.avi",cv2.cv.CV_FOURCC('F', 'M', 'P', '4'),fps,image.shape,True)
        # video_writer.open("out.mpg",cv2.cv.CV_FOURCC('M','J','P','G'),fps,image.shape,True)
        for path in image_paths:
            image = cv2.imread(path,cv2.CV_LOAD_IMAGE_GRAYSCALE)
            # cv2.waitKey(100)
            # cv2.imshow("Original", image)
            mask = image > background
            cv2.accumulateWeighted(image,image_avg,0.1,mask.astype(numpy.uint8))
            background = cv2.convertScaleAbs(image_avg)
            # cv2.imshow('Background',background)
        count = 0
        for path in image_paths:
            image = cv2.imread(path,cv2.CV_LOAD_IMAGE_GRAYSCALE)
            cv2.waitKey(100) # time to wait between frames, in mSec
            # cv2.imshow("Original", image)
            foreground = cv2.absdiff(image,background)
            # cv2.imshow('Background',background)
            # cv2.imshow('Foreground',foreground)
            ret_val,threshold = cv2.threshold(foreground,20,255,cv2.THRESH_BINARY)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
            morphed = cv2.morphologyEx(threshold,cv2.MORPH_OPEN,kernel)
            image_copy = numpy.copy(morphed)
            contours,hierarcy = cv2.findContours(image_copy,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
            image_color = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
            cv2.drawContours(image_color,contours,-1,(0,0,255),-1)

            # cv2.imshow('Threshold',threshold)
            # cv2.imshow('Morphed',morphed)
            cv2.imshow('Color',image_color)
            # video_writer.write(image_color)
            cv2.imwrite("image"+str(count)+".jpg",image_color)
            cv2.imwrite("image"+str(count+1)+".jpg",image)
            count += 2

        cv2.imwrite("background.jpg",background)
        cv2.destroyAllWindows()
        # video_writer.release()


    # def process_video(self,directory):
    #     directory = self.condition_path(directory)
    #     video = self.get_video(directory)
    #     interest_points = self.get_interest_points(directory)

    #     if DEBUG:
    #         frame_count = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    #         print("frame count: {0}".format(frame_count))
    #         fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    #         print("fps: {0}".format(fps))

    #     #     cv2.namedWindow("Original")
    #     #     cv2.namedWindow("Patches")

    #     ret, frame = video.read() # read first frame, and the return code of the function.
    #     frame_n = 0
    #     # while ret:  # note that we don't have to use frame number here, we could read from a live written file.
    #     while frame_n < 100:
    #         if frame_n == 1:
    #             self.save_image(frame,directory,"original_image1.png")
    #             print("Saved {0}/original_image1.png".format(directory))
    #             # annotated_image = self.annotate_original_image(frame,interest_points)
    #             # self.show_image(annotated_image,"Original")
    #             # self.save_image(annotated_image,directory,"annotated_image.png")
    #             patch_image = self.extract_patches(frame,interest_points)
    #             # self.show_image(patch_image,"Patches")
    #             self.save_image(patch_image,directory,"patch_image1.png")
    #             print("Saved {0}/patch_image1.png".format(directory))
    #             # self.get_gradient_data(patch_image,directory)
    #             # if DEBUG:
    #             #     # cv2.waitKey(int((1/fps)*1000)) # time to wait between frames, in mSec
    #             #     cv2.waitKey(500) # time to wait between frames, in mSec
    #         ret, frame = video.read()
    #         frame_n += 1
    #     if DEBUG:
    #         time.sleep(5)
    #         cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Track Flies')
    parser.add_argument("directory", help="Directory where image files are located")
    args = parser.parse_args()

    ft = FlyTracker()
    ft.process_images(args.directory)
