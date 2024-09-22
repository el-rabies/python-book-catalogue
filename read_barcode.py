# Importing library
import cv2
from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
import numpy as np

# Make one method to decode the barcode 
def BarcodeReader(image, isPath=False, isTest=False):
	if isPath:
		#Convert Image path to PIL and cv2 Images, decode image
		img = cv2.imread(image)
		detectedBarcodes = decode(Image.open(image))
	else:
		#decode image, convert from PIL.Image to cv2.Image
		img = np.asarray(image)
		detectedBarcodes = decode(image)
	
	# If not detected then print the message
	if detectedBarcodes != [] and isTest:
		# Traverse through all the detected barcodes in image
		for barcode in detectedBarcodes: 
			# Locate the barcode position in image
			(x, y, w, h) = barcode.rect
			
			# Put the rectangle in image using 
			# cv2 to highlight the barcode
			cv2.rectangle(img, (x-10, y-10),
						(x + w+10, y + h+10), 
						(255, 0, 0), 2)
		#Display the image
		cv2.imshow("Image", img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	return (detectedBarcodes)

if __name__ == "__main__":
# Take the image from user
	image="./barcode_1.png"
	BarcodeReader(image, True, True)
