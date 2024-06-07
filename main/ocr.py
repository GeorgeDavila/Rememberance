from PIL import Image
from paddleocr import PaddleOCR
import cv2

def runOCR_fromPath(image2processPATH, languageCode='en'):
    ocr = PaddleOCR(lang=languageCode) # need to run only once to load model into memory
    img_path = image2processPATH
    result = ocr.ocr(img_path, det=True, cls=False)
    for idx in range(len(result)):
        res = result[idx]
        #print(res)
        #for line in res:
        #    print(line)
        #    print(line[-1][0])
        allTextList = [line[-1][0] for line in res]
        #print(allTextList)

        return ' '.join(allTextList)

def runOCR_fromImageObject(cv2_image, languageCode='en'):
    ocr = PaddleOCR(lang=languageCode) # need to run only once to load model into memory
    img_path = image2processPATH
    result = ocr.ocr(img_path, det=True, cls=False)
    for idx in range(len(result)):
        res = result[idx]
        #print(res)
        #for line in res:
        #    print(line)
        #    print(line[-1][0])
        allTextList = [line[-1][0] for line in res]
        #print(allTextList)

        return ' '.join(allTextList)

#ocrOut = runOCR_fromPath(image2processPATH="testimg1.jpg", languageCode='en')
#print(ocrOut)