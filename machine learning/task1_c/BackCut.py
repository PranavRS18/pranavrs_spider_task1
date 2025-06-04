import cv2
import numpy as np

def trackbar():
    pass

#Function to Remove Background
def remove_background(img, bg_color = (0, 255, 0)):

    with_otsu =  masking(img, bg_color, otsu = True)
    without_otsu = masking(img, bg_color, otsu = False)

    mask = cv2.bitwise_or(with_otsu, without_otsu)

    mask_3ch = cv2.merge([mask, mask, mask])
    background = np.full_like(img, bg_color)
    out = np.where(mask_3ch == 255, img, background)

    return out

def masking(img, bg_color = (0, 255, 0), otsu = True):

    #Background
    bg = np.zeros_like(img)
    bg[:] = bg_color

    #Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.copyMakeBorder(gray, 10, 10, 10, 10, cv2.BORDER_REFLECT)

    #Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (19, 19), 3)

    if otsu:
        ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        ret, thresh_inv = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    else:
        ret, thresh = cv2.threshold(blurred, 223, 255, cv2.THRESH_BINARY)
        ret, thresh_inv = cv2.threshold(blurred, 223, 255, cv2.THRESH_BINARY_INV)

    # Choose Threshold with fewer white pixels
    white_binary = np.sum(thresh == 255)
    white_inv = np.sum(thresh_inv  == 255)

    if white_binary < white_inv:
        masker =  thresh_inv.copy()
    else:
        masker = thresh.copy()

    #Canny Edge Detection
    edges = cv2.Canny(masker, 50, 150)

    #Contours
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(masker, contours, -1, (0, 255, 0), -1)

    #Masking
    mask_inv = masker[10:-10, 10:-10]
    mask = cv2.bitwise_not(mask_inv)

    return mask

if __name__ == "__main__":
    #Create Windows
    cv2.namedWindow("Apple", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Dog and Cat", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Clock", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Toy", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Key", cv2.WINDOW_NORMAL)

    #Background
    color = (0, 255, 0)

    #Open Image
    image = cv2.imread("images/apple_image.jpg")

    #Remove Background
    result = remove_background(image, color)
    cv2.imshow("Apple", result)
    cv2.imwrite("results/segmented_object_1.png", result)

    #Open Image
    image = cv2.imread("images/dog-and-cat-cover.jpg")

    #Remove Background
    result = remove_background(image, color)
    cv2.imshow("Dog and Cat", result)
    cv2.imwrite("results/segmented_object_2.png", result)

    #Open Image
    image = cv2.imread("images/clock_image.jpg")

    #Remove Background
    result = remove_background(image, color)
    cv2.imshow("Clock", result)

    #Open Image
    image = cv2.imread("images/toy_image.jpg")

    #Remove Background
    result = remove_background(image, color)
    cv2.imshow("Toy", result)

    #Open Image
    image = cv2.imread("images/key.jpg")

    #Remove Background
    result = remove_background(image, color)
    cv2.imshow("Key", result)

    #Wait until a key is pressed
    cv2.waitKey(0)

    #Destroy All OpenCV Windows
    cv2.destroyAllWindows()