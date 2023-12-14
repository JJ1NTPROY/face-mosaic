# 프로젝트 개요

이 프로젝트는 Python과 OpenCV를 활용하여 사람 얼굴을 감지하고 해당 얼굴 부분을 모자이크 처리하는 오픈소스 소프트웨어입니다. 얼굴 모자이크는 사용자의 프라이버시 보호와 이미지 처리 기술을 결합하여 얼굴을 인식할 수 없게 만들어줍니다.

## 조 구성

* 202334425 김대원
* 202334511 이우정
* 202334514 이은주
* 202334496 유진규

## 사용한 패키지 및 버전

- Python (버전: 3..8.6)
- OpenCV

### 패키지 설치 방법

```bash
pip install opencv-python
```

## 사용법

1. **프로젝트 다운로드:**
   - [프로젝트 다운로드 링크](https://github.com/JJ1NTPROY/face-mosaic)에서 "Download ZIP"을 클릭하여 프로젝트를 다운로드합니다.

2. **프로젝트 압축 해제:**
   - 다운로드한 ZIP 파일을 원하는 디렉토리로 이동하여 압축을 해제합니다.

3. **Python 및 OpenCV 설치:**
   - Python이 설치되어 있지 않다면 [Python 공식 웹사이트](https://www.python.org/downloads/)에서 다운로드하고 설치합니다.
   - 터미널 또는 명령 프롬프트에서 다음 명령어를 입력하여 OpenCV를 설치합니다.
     ```bash
     pip install opencv-python
     ```

4. **이미지 모자이크 실행:**
   - 압축 해제한 프로젝트 디렉토리로 이동합니다.
   - 터미널 또는 명령 프롬프트에서 다음 명령어를 입력하여 이미지 모자이크를 실행합니다.
     ```bash
     python face_mosaic.py --input input_image.jpg --output output_image.jpg
     ```
   - `--input` 옵션으로 사용하고자 하는 이미지 파일 경로를 지정합니다.
   - `--output` 옵션으로 결과 이미지 파일을 저장할 경로를 지정합니다.

5. **결과 확인:**
   - 처리된 이미지는 `output_image.jpg`로 저장됩니다.

프로젝트는 사람 얼굴 모자이크 처리를 위한 간단하면서 효과적인 도구를 제공하며, 사용자들에게 얼굴 인식 기술에 대한 인식과 프라이버시 보호의 중요성을 강조합니다.

## 참고 자료

- [OpenCV Documentation] (https://docs.opencv.org/4.x/): OpenCV 공식 문서를 참고하여 OpenCV의 다양한 기능과 사용법을 확인할 수 있습니다.
- [Haarcascades for face detection](https://github.com/opencv/opencv/tree/master/data/haarcascades): OpenCV에서 제공하는 Haarcascades 데이터셋을 통해 얼굴 검출을 위한 학습된 모델을 확인할 수 있습니다.
이 프로젝트는 사람 얼굴 모자이크 처리를 위한 간단하면서 효과적인 도구를 제공하며, 사용자들에게 얼굴 인식 기술에 대한 인식과 프라이버시 보호의 중요성을 강조합니다.
