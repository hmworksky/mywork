import pytesseract
from PIL import Image


res = pytesseract.image_to_string(Image.open(r'D:\software\AirtestIDE_2019-01-15_py3_win64\bubble\front.air\tpl1555467747547.png'), lang='eng')
print(res)
