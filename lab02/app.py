from flask import Flask, render_template, request, jsonify
from ex01.cipher.caesar import CaesarCipher
from ex01.cipher.vigenere import VigenereCipher
from ex01.cipher.railfence import RailFenceCipher
from ex01.cipher.playfair import PlayFairCipher
from ex01.cipher.transposition import TranspositionCipher

app = Flask(__name__)

# CIPHER INSTANCES
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher("SECRET")
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()

#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/api/caesar/encrypt", methods=['POST'])
def caesar_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=['POST'])
def caesar_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


##### VIGENERE CIPHER API #####
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


##### RAILFENCE CIPHER API #####
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


##### PLAYFAIR CIPHER API #####
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})


##### TRANSPOSITION CIPHER API #####
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)