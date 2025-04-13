@echo off
echo Removing existing virtual environment if it exists...
rmdir /s /q venv

echo Creating new virtual environment with Python 3.9...
py -3.9 -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Upgrading pip and installing build tools...
python -m pip install --upgrade pip setuptools wheel

echo Installing Cython first...
python -m pip install cython==0.29.33

echo Installing Kivy dependencies...
python -m pip install kivy-deps.sdl2==0.6.0
python -m pip install kivy-deps.gstreamer==0.3.3
python -m pip install kivy-deps.glew==0.3.1
python -m pip install kivy-deps.angle==0.3.3

echo Installing Kivy...
python -m pip install kivy==2.2.1

echo Installing KivyMD...
python -m pip install kivymd==1.1.1

echo Installing other dependencies...
python -m pip install python-dotenv==1.0.0
python -m pip install requests==2.31.0
python -m pip install plyer==2.1.0
python -m pip install twilio==8.5.0
python -m pip install sqlalchemy==2.0.27
python -m pip install alembic==1.13.1
python -m pip install bcrypt==4.1.2
python -m pip install psycopg2-binary==2.9.9
python -m pip install pillow==10.2.0

echo.
echo Installation complete! The virtual environment is now ready.
echo To activate the virtual environment, run: .\venv\Scripts\activate
echo.
pause 