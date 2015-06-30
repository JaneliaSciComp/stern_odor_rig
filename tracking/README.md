tracking
========

##Install OpenCV and FlyCapture

[Install Instructions](./INSTALL_XUBUNTU.md)

##Install Dependencies

```shell
sudo apt-get install libboost-date-time-dev libboost-filesystem-dev -y
```

##Build and Create Alias

```shell
mkdir -p ~/builds/tracking/tracking-1.0
cd ~/builds/tracking/tracking-1.0
cmake ~/git/stern_odor_rig/tracking
make
echo "alias save-camera-images='$(pwd)/save-camera-images'" >> ~/.bashrc
source ~/.bashrc
ln -s "$(pwd)/save-camera-images" ~/save-camera-images
```

##Start Program

```shell
save-camera-images ~/odor_rig_data
```

##Start Saving Images

```shell
PID=`pidof save-camera-images`
kill -s USR1 $PID
```

##Stop Saving Images

```shell
PID=`pidof save-camera-images`
kill -s USR2 $PID
```

##Stop Program

Open a terminal and type:

```shell
PID=`pidof save-camera-images`
kill $PID
```
