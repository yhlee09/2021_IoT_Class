import cv2

#카메라 장치 열기
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print('Camera oepn failed')
    exit()

# fourcc(four character code) DIVX(avi) MP4V(mp4) X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, 30, (640,480))

#동영상 촬영
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame',frame)
    out.write(frame)

    if cv2.waitKey(10) == 13: # 0.01초
        break


cap.release()
out.release()
cv2.destroyAllWindows()