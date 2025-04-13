@echo off
echo Upgrading pip and installing build tools...
"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe" -m pip install --upgrade pip setuptools wheel

echo Installing Cython first...
"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe" -m pip install cython==0.29.33

echo Installing Kivy dependencies...
"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe" -m pip install kivy-deps.sdl2==0.6.0
"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe" -m pip install kivy-deps.gstreamer==0.3.3
"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe" -m pip install kivy-deps.glew==0.3.1
"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe" -m pip install kivy-deps.angle==0.3.3

echo Installing Kivy...
"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe" -m pip install kivy==2.2.1

echo Installing remaining dependencies...
"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe" -m pip install -r requirements.txt

echo Installation complete!
pause 