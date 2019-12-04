import pytesseract
from date_extractor import extract_dates
import cv2
from PIL import Image
from image_preprocessing import imgPreprocessing



def textExtraction(img):
    """
    This function detectes edges of recipt and crops it out.
    improves the quality of image by removing noise and enhancing contrast
    """
    try:  
        img=cv2.imread(img)
        preprocessedImg=imgPreprocessing(img)
        if(imgPreprocessing.status):
            text = pytesseract.image_to_string(preprocessedImg,lang='eng',config='--psm 6')
        else:
            text = pytesseract.image_to_string(img,lang='eng',config='--psm 6')

        return text
    except:
        return{"error":"Some error occures"}
	

def dateExtractor(filename):
    """
    This function will handle extracting date from text.
    """
    try:   
        text=textExtraction(filename)
        date=extract_dates(text)
        # print((date[0]))
        # dateFormated=date[0].strftime("%Y-%m-%d")
        for i in date:
            if i != 'None':
                i=i.strftime("%Y-%m-%d")
            else:
                date.remove(i)
        if len(date):
            return {'date': date }
        else:
            return {'date': 'null'}
    except:
        return{"error":"Some error occures"}


# print(dateExtractor("data/3e8b3fad.jpeg"))
