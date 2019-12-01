import pytesseract
from date_extractor import extract_dates
import cv2

from image_preprocessing import imgPreprocessing



def textExtraction(img):
    """
    This function detectes edges of recipt and crops it out.
    improves the quality of image by removing noise and enhancing contrast
    """
    # img=cv2.open(filename)
    preprocessedImg=imgPreprocessing(img)
    if(imgPreprocessing.status):
		# text = pytesseract.image_to_string(preprocessedImg,lang='eng',config='--psm 6')
        text = pytesseract.image_to_string(preprocessedImg,lang='eng',config='--psm 6')
    else:
        text = pytesseract.image_to_string(img,lang='eng',config='--psm 6')

    return text
	

def dateExtractor(filename):
    """
    This function will handle extracting date from text.
    """
    text=textExtraction(filename)
    date=extract_dates(text)
    # print((date[0]))
    dateFormated=date[0].strftime("%Y-%m-%d")
    # print(date)
    # dateFormated=map(lambda y:(y.strftime("%x")),date)
    # print(dates)
    # print("here------------------------>")
    if len(dateFormated):
        return dateFormated
    else:
        return 'null'

# print(dateExtractor("data/3e8b3fad.jpeg"))