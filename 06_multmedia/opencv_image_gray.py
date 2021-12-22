import cv2

#image 파일 읽기
img = cv2.imread('jangwonyeung.jpg')
img2 = cv2.resize(img, (600,400))

#흑백 이미지로 변환하기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#image 파일 읽기
cv2.imshow('jangwonyeung',img2)
cv2.imshow('jangwonyeung_gray',gray)

#키보드 입력 기다리기
#기본값 0,0 인 경우 키보드 입력이 있을 때까지 계속 기다림
#ENTER : 13
while True:
    if cv2.waitKey(0) == 13:
        break

cv2.imwrite('jangwonyeung.jpg',gray)

#열려있는 모든 창 닫기
cv2.destroyAllwindows() 