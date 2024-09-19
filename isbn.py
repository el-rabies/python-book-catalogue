import urllib.request

#user_input = input("Enter ISBN: ").strip()
test_isbn = "9780063237483"
api_key = "AIzaSyB2M7bkWQiYam4d09RwQvhO87c1H5if1NY"
response = urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:",test_isbn,"&api_key=" + api_key)
print(response.read().decode('utf-8'))
