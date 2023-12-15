import cv2


def detect_and_mosaic_faces(image_path):
    # 이미지 불러오기
    image = cv2.imread(image_path)
    
    # 얼굴 감지를 위한 Haarcascade 사용
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 얼굴 감지
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # 감지된 얼굴에 모자이크 처리
    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        face = cv2.resize(face, (w//10, h//10))  # 모자이크 크기 조절
        face = cv2.resize(face, (w, h), interpolation=cv2.INTER_AREA)
        image[y:y+h, x:x+w] = face
    
    # 모자이크 처리된 이미지를 반환
    return image

# 웹캠에서 영상을 읽어온다
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # WIDTH
cap.set(4, 480)  # HEIGHT

# 얼굴 인식 캐스케이드 파일 읽는다
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#video
file_path = 'video.mp4'
fps = 25.0
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
out = cv2.VideoWriter(file_path, fourcc, fps, size)

recording = False

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
        result_image = detect_and_mosaic_faces('photo.jpg')
        cv2.imwrite('mosaic pic.jpg', result_image)

    
    if ret:
        key = cv2.waitKey(50)
            
            # Check if the 'w' key is pressed (ASCII code for 'w' is 119)
        if key == 119:
            cv2.imwrite('photo.jpg', frame)
            print('Photo taken!')

        key = cv2.waitKey(50)

            # 'e' 키를 누르면 녹화 시작
        if key == ord('e') and not recording:
            recording = True
            print("녹화 시작")
            
            # 'r' 키를 누르면 녹화 종료
        elif key == ord('r') and recording:
            recording = False
            print("녹화 종료")

        if recording:
            out.write(frame)  # 파일에 프레임 저장

    if cv2.waitKey(50) & 0xFF == ord('q'):
        result_image = detect_and_mosaic_faces('photo.jpg')
        cv2.imwrite('mosaic pic.jpg', result_image)
        break
            
out.release()
cap.release()
cv2.destroyAllWindows()