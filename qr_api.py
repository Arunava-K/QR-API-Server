from flask import Flask, send_file, request
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/api/qr', methods=['GET'])
def generate_qr_code():
    url = request.args.get('url', default='', type=str)
    if not url:
        return 'Error: URL parameter is missing.', 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
