@echo off
echo Upgrading pip and installing build tools...
py -3.9 -m pip install --upgrade pip setuptools wheel

echo Installing Cython first...
py -3.9 -m pip install cython==0.29.33

echo Installing Kivy dependencies...
py -3.9 -m pip install kivy-deps.sdl2==0.6.0
py -3.9 -m pip install kivy-deps.gstreamer==0.3.3
py -3.9 -m pip install kivy-deps.glew==0.3.1
py -3.9 -m pip install kivy-deps.angle==0.3.3

echo Installing Kivy...
py -3.9 -m pip install kivy==2.2.1

echo Installing remaining dependencies...
py -3.9 -m pip install -r requirements.txt

echo Installation complete!
pause 