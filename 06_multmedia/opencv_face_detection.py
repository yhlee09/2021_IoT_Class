import cv2  

#xml 분류기 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

img = cv2.imread('Avengers.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,5)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    