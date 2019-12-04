from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import cv2
import imutils
import pytesseract

def imgPreprocessing(image):
	print("wnenverqocmq3o----",type(image))
	# print("immmmmmg",image)
	ratio = image.shape[0] / 500.0
	orig = image.copy()
	image = imutils.resize(image, height = 500)

	# convert the image to grayscale, blur it, and find edges
	# in the image
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 75, 200)

	# find the contours in the edged image, keeping only the
	# largest ones, and initialize the screen contour
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
	imgPreprocessing.status=False
	# loop over the contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)

		# if our approximated contour has four points, then we
		# can assume that we have found our screen
		if len(approx) == 4:
			screenCnt = approx
			imgPreprocessing.status=True
			warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
			warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
			T = threshold_local(warped, 11, offset = 10, method = "gaussian")
			warped = (warped > T).astype("uint8") * 255
			return warped

# cv2.imshow(imgPreprocessing("data/0a0ebd53.jpeg"))
