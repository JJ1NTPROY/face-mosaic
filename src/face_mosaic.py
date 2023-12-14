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

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 화면에 출력한다
    cv2.imshow('frame', frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

    
    if ret:
        key = cv2.waitKey(50)
            
            # Check if the 'w' key is pressed (ASCII code for 'w' is 119)
        if key == 119:
            cv2.imwrite('photo.jpg', frame)
            print('Photo taken!')
            
            
cap.release()
cv2.destroyAllWindows()