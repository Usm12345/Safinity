@echo off
echo Upgrading pip and installing build tools...
python -m pip install --upgrade pip setuptools wheel

echo Installing Cython first...
python -m pip install cython==0.29.33

echo Installing Kivy dependencies...
python -m pip install kivy-deps.sdl2==0.8.0
python -m pip install kivy-deps.gstreamer==0.3.4
python -m pip install kivy-deps.glew==0.3.1
python -m pip install kivy-deps.angle==0.4.0

echo Installing Kivy...
python -m pip install kivy==2.2.1

echo Installing remaining dependencies...
python -m pip install -r requirements.txt

echo Installation complete!
pause 