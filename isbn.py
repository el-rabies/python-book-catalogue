import urllib.request
import json
import os

def MakeBookJson(isbn):
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn + "&key=<your key>"
    urllib.request.urlretrieve(url,"./library/tmp.json")
    with open("./library/tmp.json", "r") as readFile:
        book = json.load(readFile)
        if book["totalItems"] != 0:
            title = ''.join(char for char in (book["items"][0]["volumeInfo"]["title"]) if char.isalnum())
            os.rename("./library/tmp.json", "./library/" + title + ".json")
            return(title)
        else:
            os.remove("./library/tmp.json")


#testing
if __name__ == "__main__":
    #Test with a known IBSN code
    test_isbn = "9781974743520"
    MakeBookJson(test_isbn)
