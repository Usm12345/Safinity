@echo off
echo Setting up Java environment variables...

set JAVA_HOME=D:\Safinity\jdk-11.0.2\jdk-11.0.2
set PATH=%PATH%;%JAVA_HOME%\bin

echo Java environment variables set successfully!
echo JAVA_HOME=%JAVA_HOME%

echo Testing Java installation:
"%JAVA_HOME%\bin\java" -version

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Java installation test failed. Please check your Java installation.
    exit /b 1
)

echo.
echo Java setup was successful!
echo The Java environment is now properly configured for building Android applications.
echo You may need to restart your command prompt for the changes to take effect in new sessions.