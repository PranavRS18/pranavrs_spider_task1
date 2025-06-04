import cv2
import numpy as np
from BackCut import masking

def detect_object(img):

    img_area = img.shape[0] * img.shape[1]
    with_otsu =  masking(img, otsu = True)
    without_otsu = masking(img, otsu = False)

    mask = cv2.bitwise_or(with_otsu, without_otsu)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    object_contours = []
    for contour in contours:
        if cv2.contourArea(contour) > img_area / 10:
            object_contours.append(contour)

    for object_contour in object_contours:

        min_x = np.min(object_contour[:, 0, 0])
        max_x = np.max(object_contour[:, 0, 0])
        min_y = np.min(object_contour[:, 0, 1])
        max_y = np.max(object_contour[:, 0, 1])

        cv2.rectangle(img, (min_x, min_y), (max_x, max_y), (0, 0, 255), int(img.shape[1] / 150))


    return img

if __name__ == "__main__":
    #Create Windows
    cv2.namedWindow("Apple", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Dog and Cat", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Clock", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Toy", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Key", cv2.WINDOW_NORMAL)

    #Open Image
    image = cv2.imread("images/apple_image.jpg")

    #Remove Background
    result = detect_object(image)
    cv2.imshow("Apple", result)
    cv2.imwrite("results/detected_image_1.png", result)

    #Open Image
    image = cv2.imread("images/dog-and-cat-cover.jpg")

    #Remove Background
    result = detect_object(image)
    cv2.imshow("Dog and Cat", result)
    cv2.imwrite("results/detected_image_2.png", result)

    #Open Image
    image = cv2.imread("images/clock_image.jpg")

    #Remove Background
    result = detect_object(image)
    cv2.imshow("Clock", result)

    #Open Image
    image = cv2.imread("images/toy_image.jpg")

    #Remove Background
    result = detect_object(image)
    cv2.imshow("Toy", result)

    #Open Image
    image = cv2.imread("images/key.jpg")

    #Remove Background
    result = detect_object(image)
    cv2.imshow("Key", result)

    #Wait until a key is pressed
    cv2.waitKey(0)

    #Destroy All OpenCV Windows
    cv2.destroyAllWindows()