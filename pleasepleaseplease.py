from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol

img = Image.open(r'C:\Users\tiger\Desktop\Progaming\Lib\barcode.png')

decoded_list = decode(img)

print(type(decoded_list))

print(len(decoded_list))