import cv2 as cv

img=cv.imread("img.png")
imgg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(imgg,100,255,cv.THRESH_BINARY)
contours,_ =cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
cv.drawContours(img,contours,-1,(0,255,0),1,lineType=cv.LINE_AA)
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()

