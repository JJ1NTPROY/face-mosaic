# Project outline

This project is an open-source software that uses Python and OpenCV to detect a person's face and mosaic the face part. We tried to create a program that mosaic pictures by looking at the mosaic pictures attached to the wall of the dormitory, and it combines privacy protection and image processing technology by recording videos and taking pictures of people.

## 조 구성

* 202334425 김대원: take the picture, fice-mosaic.py, managing repository
* 202334511 이우정: mosaic pic.py
* 202334514 이은주: video.py
* 202334496 유진규: person detection

## 사용한 패키지 및 버전

- Python (버전: 3..8.6)
- OpenCV

### 패키지 설치 방법

```bash
pip install opencv-python
```

## Code Description and Ouput


1. **code despription:**
-Haar classifiers, classifiers that were used in the first real-time face detector.
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
-mosaic picture

3. **Output:**
   - 처리된 이미지는 `output_image.jpg`로 저장됩니다.

프로젝트는 사람 얼굴 모자이크 처리를 위한 간단하면서 효과적인 도구를 제공하며, 사용자들에게 얼굴 인식 기술에 대한 인식과 프라이버시 보호의 중요성을 강조합니다.

## 참고 자료

- [OpenCV Documentation](https://docs.opencv.org/4.x/): OpenCV 공식 문서를 참고하여 OpenCV의 다양한 기능과 사용법을 확인할 수 있습니다.
- [Haarcascades for face detection](https://github.com/opencv/opencv/tree/master/data/haarcascades): OpenCV에서 제공하는 Haarcascades 데이터셋을 통해 얼굴 검출을 위한 학습된 모델을 확인할 수 있습니다.
이 프로젝트는 사람 얼굴 모자이크 처리를 위한 간단하면서 효과적인 도구를 제공하며, 사용자들에게 얼굴 인식 기술에 대한 인식과 프라이버시 보호의 중요성을 강조합니다.
