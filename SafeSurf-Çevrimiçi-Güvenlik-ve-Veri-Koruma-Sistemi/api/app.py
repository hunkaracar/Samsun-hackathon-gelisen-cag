from flask import Flask, request, jsonify
from flask_cors import CORS
import sifreleme
import sifreGucu 
import sts1

app = Flask(__name__)
CORS(app)

test = ""
tester = ""

@app.route('/api/veri-sifreleme', methods=['POST'])
def veri_sifreleme():
    global test, tester
    try:
        data = request.get_json()
        print("veri_sifreleme", data)
        sifreli_metin, anahtar = sifreleme.text_read(data)
        metin = str(data['text'])
        test = metin
        tester = anahtar
        return jsonify({'success': True, 'encrypted_data': sifreli_metin, 'anahtar': anahtar}), 200
    except Exception as e:
        print("Python except", e)
        return jsonify({'error': f'Hata: {str(e)}'}), 500

@app.route('/api/sifre-cozme', methods=['POST'])
def sifre_cozme():
    try:
        print("sifre_cozme çağrıldı")
        if test:
            return jsonify({'decrypted_text': test, 'anahtar': tester}), 200
        else:
            return jsonify({'error': 'Şifrelenmiş metin bulunamadı'}), 404
    except Exception as e:
        print("Python except", e)
        return jsonify({'error': f'Hata: {str(e)}'}), 500

@app.route('/api/sts', methods=['POST'])
def sts():
    try:
        data = request.get_json()
        print("sts", data)
        metin=str(data['url_or_ip'])
        print(metin)
        attack_type = sts1.text(metin)
        return jsonify({'attack_type': attack_type}), 200
    except Exception as e:
        print("Python except", e)
        return jsonify({'error': f'Hata: {str(e)}'}), 500

@app.route('/api/sifre-gucu', methods=['POST'])
def sifre_gucu():
    try:
        data = request.get_json()
        print("sifre-gucu", data)
        # Şifre gücü hesaplama işlemi yapılır
        strength = sifreGucu.text(data['password'])
        return jsonify({'strength': strength}), 200
    except Exception as e:
        print("Python except", e)
        return jsonify({'error': f'Hata: {str(e)}'}), 500

if __name__ == '_main_':
    app.run(debug=True)