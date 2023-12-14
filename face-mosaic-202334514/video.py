import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    file_path = 'video.mp4'
    fps = 25.0
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)

    out = cv2.VideoWriter(file_path, fourcc, fps, size)

    recording = False

    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow('camera-recording', frame)

            key = cv2.waitKey(1)

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

            # 'q' 키를 누르면 종료
            elif key == ord('q'):
                break
        else:
            print('no frame')
            break

    out.release()  # 파일 닫기
else:
    print("카메라를 열 수 없습니다.")

cap.release()
cv2.destroyAllWindows()
