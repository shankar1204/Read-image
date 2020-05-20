import cv2    #imporitng cv2 module

img = cv2.imread ('queeen.jpg', 1)   #declaring varaible img and passing the image path

print(img) #using print function printing the image

cv2.imshow('Resulting frame', img)  #using imshow module declare the frame name
cv2.waitKey(4000)  #using waitkey assign value
cv2.destroyAllWindows() #close all windows