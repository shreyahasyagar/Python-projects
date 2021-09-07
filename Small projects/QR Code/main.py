import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr=pyqrcode.create("Hello!")
qr.png("hello.png",scale=8)

qr1= pyqrcode.create("https://github.com/shreyahasyagar?tab=repositories")
qr1.png("githubprofile.png",scale=8)

d=decode(Image.open("githubprofile.png"))
print(d[0].data.decode("ascii"))