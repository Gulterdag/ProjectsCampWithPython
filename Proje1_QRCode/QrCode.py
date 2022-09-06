import qrcode

code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=2
)
code.add_data('https://www.youtube.com/watch?v=rrk-zuuc77U')
code.make(fit=True)

image = code.make_image(fill_color="white", back_color="red")
image.save('QRCode.png')