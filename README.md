If using ubuntu first remove libqt5x11extras5 (otherwise it won't work due to QT conflicts).


```
sudo apt-get install -y libopencv-dev gphoto2 v4l2loopback-utils ffmpeg
pip uninstall -y opencv-python opencv-contrib-python
pip install opencv-python opencv-contrib-python
```

