import qrcode


def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,

    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_colour = "black",back_colour = "white")
    img.save("qrimg.png")


url = input("enter your url: ")
generate_qrcode(url)