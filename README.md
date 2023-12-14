# 프로젝트 개요

이 프로젝트는 Python과 OpenCV를 활용하여 사람 얼굴을 감지하고 해당 얼굴 부분을 모자이크 처리하는 오픈소스 소프트웨어입니다. 얼굴 모자이크는 사용자의 프라이버시 보호와 이미지 처리 기술을 결합하여 얼굴을 인식할 수 없게 만들어줍니다.

## 데모나 예시

프로젝트 예시 이미지는 [여기](예시 이미지 링크)에서 확인할 수 있습니다.

## 사용한 패키지 및 버전

- Python (버전: 3..8.6)
- OpenCV

### 패키지 설치 방법

```bash
pip install opencv-python
```

### 프로젝트 실행 스크립트

프로젝트를 클론하고 실행하기 위한 Bash 스크립트입니다.

1. **프로젝트 클론:**

    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```

    - `git clone` 명령어를 사용하여 프로젝트를 복제합니다.
    - `cd` 명령어를 사용하여 프로젝트 디렉토리로 이동합니다.

2. **의존성 설치:**

    ```bash
    pip install -r requirements.txt
    ```

    - `pip install` 명령어를 사용하여 프로젝트에 필요한 의존성을 설치합니다.

3. **이미지 모자이크 실행:**

    ```bash
    python face_mosaic.py --input input_image.jpg --output output_image.jpg
    ```

    - `python` 명령어를 사용하여 `face_mosaic.py` 스크립트를 실행합니다.
    - `--input` 옵션으로 입력 이미지 파일 경로를 지정합니다.
    - `--output` 옵션으로 결과 이미지 파일 경로를 지정합니다.

4. **결과 확인:**

    - 처리된 이미지는 `output_image.jpg`로 저장됩니다.

위 스크립트는 프로젝트를 설정하고 실행하는 간단한 방법을 제공합니다.

## 참고 자료

- [OpenCV Documentation] (https://docs.opencv.org/4.x/): OpenCV 공식 문서를 참고하여 OpenCV의 다양한 기능과 사용법을 확인할 수 있습니다.
- [Haarcascades for face detection](https://github.com/opencv/opencv/tree/master/data/haarcascades): OpenCV에서 제공하는 Haarcascades 데이터셋을 통해 얼굴 검출을 위한 학습된 모델을 확인할 수 있습니다.
이 프로젝트는 사람 얼굴 모자이크 처리를 위한 간단하면서 효과적인 도구를 제공하며, 사용자들에게 얼굴 인식 기술에 대한 인식과 프라이버시 보호의 중요성을 강조합니다.
