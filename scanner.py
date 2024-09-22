import cv2
from PIL import Image
from read_barcode import BarcodeReader

def getBarcodesList():
    barcodeList = []
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        #Display What the camera is seeing
        cv2.imshow("preview", frame)
        rval, frame = vc.read()

        key = cv2.waitKey(20)

        #Register Barcodes on SPACE key
        if key == 32:
            #Convert the cv2-Image "frame" to a PIL image and Pass to Barcode reader
            PILimg = Image.fromarray(frame)
            newBarcode = BarcodeReader(PILimg)
            if newBarcode != []:
                barcodeList.append(newBarcode)
                for barcode in newBarcode:
                    (x, y, w, h) = barcode.rect
                    cv2.rectangle(frame, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 5)
        
        #Exit on ESC key
        if key == 27:
            break   

    vc.release()
    cv2.destroyWindow("preview")
    return(barcodeList)


if __name__ == "__main__":
    #Testing
    print(getBarcodesList())