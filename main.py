import json
from scanner import getBarcodesList
from isbn import MakeBookJson
from update_libFile import UpdateLibFile

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

newFileNames = []

for data in dataList:
    tmp = str(data)
    tmp2 = tmp[1:]
    isbn = ''.join(tmp2.split('\'',2))
    newFileNames.append(MakeBookJson(isbn))

for newfile in newFileNames:
    with open("./library/" + newfile + ".json", "r") as readFile:
        book = json.load(readFile)
        if book["totalItems"] != 0:
            try:
                title = book["items"][0]["volumeInfo"]["title"]
            except Exception as err:
                title = "Not Found"
            
            try:
                author = book["items"][0]["volumeInfo"]["authors"][0]
            except Exception as err:
                author = "Not Found"
            try:
                publishedDate = book["items"][0]["volumeInfo"]["publishedDate"]
            except Exception as err:
                publishedDate = "Not Found"
            
            try:
                genre = book["items"][0]["volumeInfo"]["categories"][0]
            except Exception as err:
                genre = "Not Found"
            try:
                pageCount = book["items"][0]["volumeInfo"]["pageCount"]
            except Exception as err:
                pageCount = "Not Found"

            bookData = {'Title':[title], 
                        'Author':[author], 
                        'Publishing Date':[publishedDate],
                        'Genre':[genre],
                        'Page Count':[pageCount]
                    }
            
            UpdateLibFile(bookData)