import qrcode
import image

img = qrcode.make("test")
img.save("test.jpg")

