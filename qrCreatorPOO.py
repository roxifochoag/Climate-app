import qrcode

class QRCodeGenerator:
    def __init__(self, data):
        self.data = data

    def generate_qr_code(self, filename):
        img = qrcode.make(self.data)
        img.save(filename)
        print(f"El código QR se llama  {filename}")

# Uso de la clase
if __name__ == "__main__":
    data = 'test'
    generator = QRCodeGenerator(data)
    generator.generate_qr_code('test.png')
