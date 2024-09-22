This project allows you to quickly catalogue the books you own by scanning ISBN codes and gathering data into an excel file.
It works for macOS by default, changing the paths in main.py, isbn.py and update_libFile.py allows to it to work on windows.

**All Dependencies**<br />
brew install zbar<br />
pip install pyzbar<br />
pip install pillow<br />
pip install opencv-python<br />
pip install urllib3<br />
pip install openpyxl<br />
pip install json<br />
pip install pandas<br />
pip install os<br />
pip install numpy<br />

**To Run: one of these will probably work**<br />
python *path_to*/main.py<br />
python3 *path_to*/main.py<br />
