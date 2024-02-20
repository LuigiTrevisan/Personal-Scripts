set CURRENT_DIR=%~dp0

pyinstaller --noconfirm --clean --onefile --console --icon "%CURRENT_DIR%\icon.ico"  "%CURRENT_DIR%\duplicateremover.py"
rmdir /s /q "%CURRENT_DIR%\build"
move "%CURRENT_DIR%\dist\duplicateremover.exe" "%CURRENT_DIR%"
rmdir /s /q "%CURRENT_DIR%\dist"
del "%CURRENT_DIR%\duplicateremover.spec"