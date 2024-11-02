import qrcode

img = qrcode.make('https://github.com/techleonic')
img.save("qr1.png")


