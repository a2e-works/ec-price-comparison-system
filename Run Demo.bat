@echo off
title EC Price Comparison System Demo
color 0A

echo.
echo =====================================================
echo         EC Price Comparison System Demo
echo =====================================================
echo.

echo [1/5] Loading sample product list...
timeout /t 1 >nul

echo [2/5] Retrieving marketplace prices...
timeout /t 1 >nul

echo     Amazon    OK
echo     Rakuten   OK
echo     Yahoo     OK
echo.

echo [3/5] Calculating profit rates...
timeout /t 1 >nul

echo [4/5] Generating Excel report...
python demo\price_comparison_demo.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo **********************************************
    echo ERROR : Demo execution failed.
    echo Please check your Python environment.
    echo **********************************************
    pause
    exit /b
)

echo.
echo [5/5] Completed successfully!
echo.
echo Output file:
echo sample\sample_output.xlsx
echo.
echo Thank you for trying this portfolio demo.
echo.

pause
