@echo off
setlocal enabledelayedexpansion
set PYTHON_PATH=Python
set SCRIPT_PATH="load_the_saved_model.py"

:run_loop
%PYTHON_PATH% %SCRIPT_PATH%