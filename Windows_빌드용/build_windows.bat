@echo off
chcp 65001 >nul
echo ========================================
echo  CU 발주시스템 Windows 빌드 스크립트
echo ========================================
echo.

REM PyInstaller 설치 확인
python --version >nul 2>&1
if errorlevel 1 (
    echo [오류] Python이 설치되어 있지 않습니다.
    echo Python 3.7 이상을 설치해주세요.
    pause
    exit /b 1
)

echo [1/3] PyInstaller 설치 확인 중...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller가 설치되어 있지 않습니다. 설치 중...
    pip install pyinstaller
    if errorlevel 1 (
        echo [오류] PyInstaller 설치에 실패했습니다.
        pause
        exit /b 1
    )
) else (
    echo PyInstaller가 이미 설치되어 있습니다.
)

echo.
echo [2/3] 이전 빌드 파일 정리 중...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist CU발주시스템.spec del /q CU발주시스템.spec

echo.
echo [3/3] Windows 실행 파일 생성 중...
pyinstaller --onefile --name "CU발주시스템" --console calculator_cu.py

if errorlevel 1 (
    echo [오류] 빌드에 실패했습니다.
    pause
    exit /b 1
)

echo.
echo ========================================
echo  빌드 완료!
echo ========================================
echo.
echo 실행 파일 위치: dist\CU발주시스템.exe
echo.
echo 배포 시 dist 폴더의 내용을 압축하여 배포하세요.
echo.
pause

