from scanner import getBarcodesList
from isbn import MakeBookJson
#Initialize list of barcode groups
barcodesListList = []

#scan for barcodes using function
newBarcodes = getBarcodesList()
if newBarcodes != []:
    barcodesListList.append(newBarcodes)

#Collect codes from barcodes
dataList = []
for barcodesList in barcodesListList:
    for barcodes in barcodesList:
        for barcode in barcodes:
            if barcode.type =="EAN13":
                dataList.append(barcode.data)

for data in dataList:
    tmp = str(data)
    tmp2 = tmp[1:]
    isbn = ''.join(tmp2.split('\'',2))
    MakeBookJson(isbn)

