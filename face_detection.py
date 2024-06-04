import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()

    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face = haar_cascade.detectMultiScale(grayImg,1.3,4)

    for (x,y,w,h) in face:
        
        x1,y1=x+w, y+h

        cv2.line(img, (x,y), (x+30, y),(0, 255, 0), 6)
        cv2.line(img, (x,y), (x, y+30),(0, 255, 0), 6)

        cv2.line(img, (x1,y), (x1-30, y),(0, 255, 0), 6)
        cv2.line(img, (x1,y), (x1, y+30),(0, 255, 0), 6)

        cv2.line(img, (x,y1), (x+30, y1),(0, 255, 0), 6)
        cv2.line(img, (x,y1), (x, y1-30),(0, 255, 0), 6)

        cv2.line(img, (x1,y1), (x1-30, y1),(0, 255, 0), 6)
        cv2.line(img, (x1,y1), (x1, y1-30),(0, 255, 0), 6)
        
    cv2.imshow("Face Detection",img)

    key = cv2.waitKey(10)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
