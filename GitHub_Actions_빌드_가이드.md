# GitHub Actions로 Windows 실행 파일 만들기 (Windows PC 없이 가능!)

## 🎯 이 방법의 장점
- ✅ Windows PC 불필요
- ✅ 완전 자동화
- ✅ 언제든지 재빌드 가능
- ✅ 무료

## 📋 준비사항
- GitHub 계정 (무료로 만들 수 있음)
- 인터넷 연결

## 🚀 단계별 가이드

### 1단계: GitHub 저장소 만들기

1. https://github.com 에서 로그인 (계정이 없으면 회원가입)
2. 우측 상단 "+" 버튼 클릭 → "New repository"
3. 저장소 이름 입력 (예: `CU발주시스템`)
4. "Public" 또는 "Private" 선택
5. "Create repository" 클릭

### 2단계: 파일 업로드

방법 A: 웹에서 직접 업로드 (간단)
1. 저장소 페이지에서 "uploading an existing file" 클릭
2. 다음 파일들을 드래그 앤 드롭:
   - `calculator_cu.py`
   - `.github/workflows/build_windows.yml` (폴더 포함)
3. "Commit changes" 클릭

방법 B: Git 사용 (고급)
```bash
git init
git add calculator_cu.py .github/
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/사용자명/CU발주시스템.git
git push -u origin main
```

### 3단계: 빌드 실행

1. GitHub 저장소 페이지에서 "Actions" 탭 클릭
2. 왼쪽에서 "Build Windows Executable" 워크플로우 선택
3. "Run workflow" 버튼 클릭
4. "Run workflow" 다시 클릭하여 실행

### 4단계: 실행 파일 다운로드

1. 빌드가 완료될 때까지 대기 (약 2-3분)
2. 완료되면 "CU발주시스템_Windows" Artifact 클릭
3. "CU발주시스템.exe" 파일 다운로드

## 📦 배포 준비

다운로드한 파일:
- `CU발주시스템.exe`
- `Windows_사용설명서.txt` (dist 폴더에 있음)

이 두 파일을 압축하여 배포하세요!

## 🔄 재빌드가 필요한 경우

`calculator_cu.py` 파일을 수정한 후:
1. GitHub에 파일 업로드 (또는 push)
2. Actions 탭에서 워크플로우 다시 실행
3. 새로 빌드된 .exe 파일 다운로드

## ❓ 문제 해결

**워크플로우가 보이지 않아요**
- `.github/workflows/build_windows.yml` 파일이 제대로 업로드되었는지 확인
- 파일 경로가 정확한지 확인

**빌드가 실패해요**
- Actions 탭에서 빌드 로그 확인
- 오류 메시지 확인 후 수정

**다운로드가 안 돼요**
- 브라우저를 새로고침
- 다른 브라우저로 시도

## 💡 팁

- 저장소를 Private으로 만들어도 Actions는 무료로 사용 가능합니다
- 빌드 이력은 모두 저장되므로 언제든지 이전 버전을 다운로드할 수 있습니다

