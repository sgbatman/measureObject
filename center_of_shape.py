# import the necessary packages
import imutils
import cv2

# load the image, convert it to grayscale, blur it slightly then thresh make image to black and white
image = cv2.imread("image/shapes_and_colors.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the threshold-ed image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)
    m10 = M["m10"]
    m00 = M["m00"]
    m01 = M["m01"]
    m00 = M["m00"]

    if m10 and m00 and m01 and m00 > 0:
        cX = int(m10 / m00)
        cY = int(m01 / m00)

        # draw the contour and center of the shape on the image
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# show the image
cv2.imshow("Image", image)
cv2.waitKey(0)
