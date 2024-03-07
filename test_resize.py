import os
import shutil
import cv2 #import the library opencv
import glob #globbing utility.

A = "D:/THEKKBox/dev/resize images/images/*"
for file in glob.glob(A):
    print(file)
    a = cv2.imread(file)
    print(a)

    #conversion numpy array into rgb image to show
    b = cv2.resize(a,(189,252))
    cv2.imshow('show image', b)
    cv2.imwrite(file,b)
    k = cv2.waitKey(1000) #wait for 1 second
    cv2.destroyAllWindows() #destroy the window