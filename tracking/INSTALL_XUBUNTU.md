Installation Xubuntu
====================


###Install Xubuntu

<http://xubuntu.org/getxubuntu/>

Install Latest LTS release: 14.04, Trusty Tahr

```shell
sudo apt-get update
sudo apt-get dist-upgrade -y
sudo apt-get install git openssh-server -y
```

###Install Point Grey FlyCapture2 Library

Links and instructions for downloading and installing the latest
FlyCapture 2.x library from Point Grey for Linux can be found here:

<http://www.ptgrey.com/support/downloads>

Download Linux (64-bit, 32-bit, or ARM, whichever is appropriate).
Requires registration.

```shell
cd ~/Downloads
tar -zxvf flycapture*
cd flycapture*
cat README
# follow the instructions that the script takes you through
sudo reboot
```

###Test Point Grey FlyCapture2 Library

```shell
# plug in Flea3 camera into USB3 port
flycap
```

```shell
cp -r /usr/src/flycapture/src/ ~/flycapture_examples
mkdir ~/bin
mkdir ~/lib
cd ~/flycapture_examples/FlyCapture2Test
make
mkdir ~/Pictures/FlyCapture2Test
# plug in Flea3 camera into USB3 port
cd ~/Pictures/FlyCapture2Test
~/bin/FlyCapture2Test
```

###Download, Configure, and Build OpenCV

```shell
sudo apt-get install build-essential checkinstall libgtk2.0-dev libjpeg-dev libtiff4-dev libjasper-dev libopenexr-dev cmake python-dev python-numpy python-tk libtbb-dev libeigen3-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev libqt4-dev libqt4-opengl-dev sphinx-common texlive-latex-extra libv4l-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev default-jdk ant libvtk5-qt4-dev
mkdir ~/git
cd ~/git
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout -b 2.4 origin/2.4
mkdir -p ~/builds/opencv/opencv-2.4
cd ~/builds/opencv/opencv-2.4
cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_VTK=ON  ~/git/opencv
make -j2
sudo checkinstall
```

To uninstall:

```shell
sudo dpkg -r opencv
```
