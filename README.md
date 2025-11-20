# CU 발주시스템

편의점 자동 발주 계산 시스템

## 📦 배포용 파일

### Windows 사용자용
- `CU발주시스템.exe` - 실행 파일 (Windows PC에서 빌드 필요)
- `Windows_사용설명서.txt` - 사용 안내서

### macOS 사용자용  
- `CU발주시스템` - 실행 파일 (dist 폴더)
- `사용설명서.txt` - 사용 안내서

## 🚀 Windows 실행 파일 빌드 방법

### 옵션 1: GitHub Actions (권장)
1. 이 저장소를 GitHub에 업로드
2. Actions 탭에서 워크플로우 실행
3. Artifacts에서 .exe 파일 다운로드

### 옵션 2: Windows PC에서 빌드
1. `build_windows.bat` 실행
2. `dist/CU발주시스템.exe` 생성

## 📝 사용 방법

1. 실행 파일 더블클릭
2. 참고일의 판매량 입력
3. 발주 결과 확인

## ⚠️ 주의사항

- Windows용 .exe는 Windows PC에서만 빌드 가능합니다
- macOS에서는 Windows용 실행 파일을 만들 수 없습니다
- GitHub Actions를 사용하면 Windows PC 없이도 빌드 가능합니다

