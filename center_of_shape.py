# import the necessary packages
import imutils
import cv2


def resize_image(img_src, scale_percent):
    """
    Take in src and scale percent as args, return numpy.ndarray aka. image.

    Keyword arguments:
    img_src -- image to be re sized
    scale_percent -- the percentage to be resize
    """
    # calculate the given percent of original dimensions
    width = int(img_src.shape[1] * scale_percent / 100)
    height = int(img_src.shape[0] * scale_percent / 100)

    # desired size
    dsize = (width, height)

    # return re sized image
    return cv2.resize(image, dsize)


# load the image, convert it to grayscale, blur it slightly then thresh make image to black and white
image = cv2.imread("image/shapes.jpg", cv2.IMREAD_UNCHANGED)

resize_image(image, 20)
output = resize_image(image, 20)
print(type(output))

cv2.imshow("Resized Images", output)
cv2.waitKey(0)

gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blur, 145, 255, cv2.THRESH_BINARY_INV)[1]

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
        cv2.drawContours(output, [c], -1, (0, 255, 0), 2)
        cv2.circle(output, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(output, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# show the image
cv2.imshow("Images", output)
cv2.waitKey(0)
