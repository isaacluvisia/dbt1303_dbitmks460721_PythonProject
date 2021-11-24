#For QR code generation using python, we are going to use a python module called QRcode.
#Install it using this command: pip install qrcode
#This is for converting the captioned link to qr code

import qrcode
img = qrcode.make("https://www.youtube.com/")
img.save("youtubeQR.jpg")

#This is for converting the sentence to qr code
import qrcode
img = qrcode.make("India is a country with many religions. I love India.")
img.save("youtubeQR.jpg")

#Code to decode a QR code back to know the original string.
#Install opencv: pip install opencv-python
import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("myQRCode.jpg"))
print("Decoded text is: ", val)