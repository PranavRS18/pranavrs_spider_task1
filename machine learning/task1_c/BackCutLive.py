import cv2
import numpy as np

#WebCam
capture = cv2.VideoCapture(0)
fourcc = getattr(cv2, 'VideoWriter_fourcc')(*'mp4v')
video = cv2.VideoWriter('results/realtime_background_removed.mp4', fourcc, 10.0, (640, 480))

#Function to Remove Background
def remove_background(img, bg_color):

    #Background
    bg = np.zeros_like(img)
    bg[:] = bg_color

    #Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.copyMakeBorder(gray, 10, 10, 10, 10, cv2.BORDER_REFLECT)

    #Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (19, 19), 3)

    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    masker = thresh.copy()

    #Canny Edge Detection
    edges = cv2.Canny(masker, 50, 150)

    #Contours
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(masker, contours, -1, (0, 255, 0), -1)

    #Masking
    mask_inv = masker[10:-10, 10:-10]
    mask = cv2.bitwise_not(mask_inv)

    mask_3ch = cv2.merge([mask, mask, mask])
    background = np.full_like(img, bg_color)
    out = np.where(mask_3ch == 255, img, background)

    return out

#Capture Loop
while True:
    #Get Frames
    ret, frame = capture.read()
    if not ret:
        print("No Frames")
        break

    new_frame = remove_background(frame, (0, 255, 0))
    video.write(new_frame)
    cv2.imshow("BackCutLive", new_frame)
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

capture.release()
video.release()

#Destroy All OpenCV Windows
cv2.destroyAllWindows()