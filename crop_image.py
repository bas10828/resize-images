import cv2


def main():
    #Crop Image Demo
    image = cv2.imread("image.jpg")
    dimension = image.shape
    height = dimension[0]
    width = dimension[1]
    cropped_image = image[0:(height),280:(width-280)]
    cv2.imwrite("croppedimage.jpg",cropped_image)
    print("halt")

if __name__ == '__main__':
    main()