# GitHub Actions 워크플로우 수동 생성 가이드

## 문제: 워크플로우가 보이지 않을 때

GitHub에서 워크플로우가 보이지 않는다면, 워크플로우 파일이 제대로 업로드되지 않았을 수 있습니다.

## 해결 방법: 워크플로우 파일 수동 생성

### 1단계: GitHub 저장소에서 파일 생성

1. GitHub 저장소 페이지로 이동
2. "Add file" → "Create new file" 클릭
3. 파일 경로 입력: `.github/workflows/build_windows.yml`
   - ⚠️ 중요: `.github` 앞에 점(.)이 있어야 합니다!
   - 경로를 입력하면 자동으로 폴더가 생성됩니다

### 2단계: 워크플로우 내용 복사

아래 내용을 모두 복사하여 붙여넣기:

```yaml
name: Build Windows Executable

on:
  workflow_dispatch:
  push:
    branches:
      - main
    paths:
      - 'calculator_cu.py'

jobs:
  build:
    runs-on: windows-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install PyInstaller
      run: pip install pyinstaller
    
    - name: Build executable
      run: |
        pyinstaller --onefile --name "CU발주시스템" --console calculator_cu.py
    
    - name: Upload artifact
      uses: actions/upload-artifact@v3
      with:
        name: CU발주시스템_Windows
        path: dist/CU발주시스템.exe
```

### 3단계: 파일 저장

1. 페이지 하단의 "Commit new file" 클릭
2. 커밋 메시지 입력 (예: "Add Windows build workflow")
3. "Commit new file" 클릭

### 4단계: 워크플로우 실행

1. 저장소 상단의 "Actions" 탭 클릭
2. 이제 "Build Windows Executable" 워크플로우가 보일 것입니다!
3. "Build Windows Executable" 클릭
4. "Run workflow" 버튼 클릭
5. "Run workflow" 다시 클릭하여 실행

## 확인 사항

워크플로우 파일이 제대로 생성되었는지 확인:
- 저장소에서 `.github/workflows/build_windows.yml` 파일이 보여야 합니다
- 파일 내용이 위의 YAML 코드와 일치해야 합니다

## 여전히 안 보이면?

1. 브라우저 새로고침 (F5)
2. 다른 브라우저로 시도
3. GitHub 저장소를 Private으로 만들었는지 확인 (Private도 Actions 사용 가능)

