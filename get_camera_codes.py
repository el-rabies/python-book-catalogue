import cv2
from PIL import Image
from read_barcode import BarcodeReader

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    #Display What the camera is seeing
    cv2.imshow("preview", frame)

    #Convert the cv2-Image "frame" to a PIL image and Pass to Barcode reader
    PILimg = Image.fromarray(frame)
    BarcodeList = BarcodeReader(PILimg)
    
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("preview")