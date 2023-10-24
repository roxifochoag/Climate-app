import qrcode
import cv2

class QRCodeGenerator:
    def __init__(self, data):
        self.data = data

    def generate_qr_code(self, filename):
        img = qrcode.make(self.data)
        img.save(filename)
        print(f"QR codigo grabado como {filename}")

    def decode_qr_code(self, filename):
        img = cv2.imread(filename)
        detector = cv2.QRCodeDetector()
        value, _, _ = detector.detectAndDecode(img)
        return value

# Uso de la clase
if __name__ == "__main__":
    data = 'test'
    generator = QRCodeGenerator(data)
    generator.generate_qr_code('test.png')
    decoded_data = generator.decode_qr_code('test.png')
    print(f"Data decodificada data: {decoded_data}")
