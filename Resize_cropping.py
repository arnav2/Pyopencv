import cv2 
image= cv2.imread("Capture.jpg")
cv2.imshow("new", image)#not necessary just to show the read image 
cv2.waitkey(0)#Press 0 to exit the image 
print image.shape #gives us the dimension of the image 
######## Naive Way ####################################
#dim=((image.shape[1]/100),int((image.shape[0])/100))
##########Better Way ###################################
r = 100.0/image.shape[1]
dim = (100, int(image.shape[0]*r))

#Resizing the images (other types of resizing) 
#INTER_NEAREST 
#INTER_LINEAR 
#INTER_CUBIC 
#INTER_LANCZOS4
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized",resized)
cv2.waitkey(0)

###Cropping the image #######
cropped = image [70: 170 , 440:540]
cv2.imshow("cropped image", cropped)
cv2.waitkey(0)

####Writing on the disk####### 
cv2.imwrite("blah",cropped)

