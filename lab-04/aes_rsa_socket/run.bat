@echo off
REM 🔐 Secure Chat - AES-RSA Encrypted Communication
REM Run script for Windows

title Secure Chat - Socket + Web Server

echo.
echo ============================================================
echo  ^🔐 SECURE CHAT - AES-RSA Encrypted Communication
echo ============================================================
echo.
echo Starting application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

REM Run the secure chat application
python run.py

pause
