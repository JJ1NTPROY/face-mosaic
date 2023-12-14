import cv2

# 웹캠에서 영상을 읽어온다
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # WIDTH
cap.set(4, 480)  # HEIGHT

# 얼굴 인식 캐스케이드 파일 읽는다
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # frame 별로 capture 한다
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 인식된 얼굴 갯수를 출력
    print(len(faces))

    # 인식된 얼굴에 약한 모자이크를 적용한다
    for (x, y, w, h) in faces:
        # 얼굴 부분을 추출
        face_roi = frame[y:y+h, x:x+w]

        # 약한 모자이크를 위해 큰 값으로 설정
        face_roi = cv2.resize(face_roi, (0, 0), fx=0.08, fy=0.08)  # 얼굴 부분 축소
        face_roi = cv2.resize(face_roi, (w, h), interpolation=cv2.INTER_LINEAR)  # 원래 크기로 확대

        frame[y:y+h, x:x+w] = face_roi

    # 화면에 출력한다
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()