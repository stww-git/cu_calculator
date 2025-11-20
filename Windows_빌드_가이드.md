# Windows 실행 파일 빌드 가이드

## 방법 1: GitHub Actions 사용 (Windows PC 없이 가능) ⭐

### 준비사항
- GitHub 계정

### 단계
1. GitHub에 새 저장소 생성
2. 이 폴더의 모든 파일을 업로드
3. Actions 탭에서 "Build Windows Executable" 워크플로우 실행
4. 완료 후 Artifacts에서 `CU발주시스템.exe` 다운로드

### 장점
- Windows PC 불필요
- 자동 빌드
- 언제든지 재빌드 가능

---

## 방법 2: Windows PC에서 직접 빌드

### 준비사항
- Windows PC
- Python 3.7 이상

### 단계
1. `build_windows.bat` 파일 더블클릭
2. 자동으로 빌드 진행
3. `dist` 폴더에 `CU발주시스템.exe` 생성

---

## 방법 3: 온라인 서비스 사용

다음 서비스를 사용할 수도 있습니다:
- Replit (온라인 IDE)
- CodeSpaces (GitHub)
- 기타 클라우드 빌드 서비스

---

## 배포 패키지 구성

빌드 완료 후 다음 파일들을 압축하여 배포:

```
CU발주시스템_Windows.zip
├── CU발주시스템.exe
└── Windows_사용설명서.txt
```

사용자는 압축을 풀고 `CU발주시스템.exe`를 더블클릭하면 됩니다!

