import qrcode
def newQR(text):
    # Link for website
    input_data = text
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    imgName = 'qrcode001.png'
    img.save(imgName)
    return imgName