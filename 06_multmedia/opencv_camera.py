import cv2

#카메라 장치 열기
cap = cv2.VideoCapture(output.avi) #'output.avi'

if not cap.isOpened():
    print('Camera oepn failed')
    exit()

#카메라 사진 찍기
ret, frame = cap.read()

cv2.imshow('frame',frame)
cv2.imwrite('output.jpg',frame)

cv2.waitkey(10000) #10초

# #동영상 촬영
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     cv2.imshow('frame',frame)

#     if cv2.waitKey(10) == 13: # 0.01초
#         break


cap.release()
cv2.destroyAllWindows()