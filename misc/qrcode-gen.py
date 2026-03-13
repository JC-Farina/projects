import qrcode


def gen_qr_code(url, name='default.png' , fill_color='black', back_color='white'):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.show()  # Display the QR code
    img.save(name)  # Save the QR code as a PNG file

if __name__ == "__main__":
    url = input("Enter the link or text to generate QR code: ")
    fill_color = input("Enter the fill color (default is 'black'): ") or 'black'
    back_color = input("Enter the background color (default is 'white'): ") or 'white'
    name = input('Enter name: ')

    gen_qr_code(url, name, fill_color, back_color)
