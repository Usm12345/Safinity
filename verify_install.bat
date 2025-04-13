@echo off
echo Checking Python version...
"C:\Users\OK\AppData\Local\Programs\Python\Python311\python.exe" --version

echo.
echo Checking installed packages...
"C:\Users\OK\AppData\Local\Programs\Python\Python311\python.exe" -m pip list

echo.
echo Testing Kivy installation...
"C:\Users\OK\AppData\Local\Programs\Python\Python311\python.exe" -c "import kivy; print('Kivy version:', kivy.__version__)"

pause 