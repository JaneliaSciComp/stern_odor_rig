tracking
========

Install OpenCV and FlyCapture
-----------------------------

[Install Instructions](./INSTALL_XUBUNTU.md)

Build and Create Alias
----------------------

```shell
mkdir -p ~/builds/tracking/tracking-1.0
cd ~/builds/tracking/tracking-1.0
cmake ~/git/stern_odor_rig/tracking
make
echo "alias tracking='$(pwd)/tracking'" >> ~/.bashrc
source ~/.bashrc
```

Run
---

```shell
tracking ~/odor_rig_data
```
