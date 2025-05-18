@echo off
setlocal

rem Create folders
mkdir project
mkdir project\templates
mkdir project\static

rem Create files
type nul > project\app.py
type nul > project\templates\index.html
type nul > project\templates\login.html
type nul > project\templates\messages.html
type nul > project\templates\404.html
type nul > project\templates\500.html
type nul > project\static\style.css
type nul > project\static\script.js
type nul > project\requirements.txt
type nul > project\messages.db

echo Folders and files created successfully!
pause
endlocal
