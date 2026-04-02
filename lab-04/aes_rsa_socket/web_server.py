from flask import Flask, render_template, request, jsonify, session
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import json
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-secure-chat-2024'

# Global variables for managing multiple users
user_sockets = {}  # {user_id: SocketManager}
messages_history = []  # Shared message history
messages_lock = threading.Lock()

class SocketManager:
    def __init__(self):
        self.socket = None
        self.aes_key = None
        self.client_key = None
        self.is_connected = False
        
    def connect_to_server(self, host='localhost', port=12345):
        """Connect to the AES-RSA socket server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
            
            # Generate RSA key pair
            self.client_key = RSA.generate(2048)
            
            # Receive server's public key
            server_public_key_data = self.socket.recv(2048)
            server_public_key = RSA.import_key(server_public_key_data)
            
            # Send client's public key to the server
            self.socket.send(self.client_key.publickey().export_key(format='PEM'))
            
            # Receive encrypted AES key from the server
            encrypted_aes_key = self.socket.recv(2048)
            
            # Decrypt the AES key using client's private key
            cipher_rsa = PKCS1_OAEP.new(self.client_key)
            self.aes_key = cipher_rsa.decrypt(encrypted_aes_key)
            
            self.is_connected = True
            return True, "Connected to server successfully"
        except Exception as e:
            self.is_connected = False
            return False, str(e)
    
    def encrypt_message(self, message):
        """Encrypt message using AES"""
        if not self.aes_key:
            return None
        cipher = AES.new(self.aes_key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
        return cipher.iv + ciphertext
    
    def decrypt_message(self, encrypted_message):
        """Decrypt message using AES"""
        if not self.aes_key:
            return None
        iv = encrypted_message[:AES.block_size]
        ciphertext = encrypted_message[AES.block_size:]
        cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_message.decode()
    
    def send_message(self, message):
        """Send encrypted message to server"""
        if not self.is_connected:
            return False, "Not connected to server"
        try:
            encrypted_msg = self.encrypt_message(message)
            self.socket.send(encrypted_msg)
            return True, "Message sent"
        except Exception as e:
            return False, str(e)
    
    def receive_message(self):
        """Receive encrypted message from server"""
        if not self.is_connected:
            return None
        try:
            encrypted_message = self.socket.recv(1024)
            if encrypted_message:
                decrypted_msg = self.decrypt_message(encrypted_message)
                return decrypted_msg
        except Exception as e:
            print(f"Error receiving message: {e}")
        return None
    
    def disconnect(self):
        """Disconnect from server"""
        if self.socket:
            self.socket.close()
        self.is_connected = False

# Function to receive messages for a specific user
def receive_messages_thread(user_id, socket_manager):
    """Background thread to receive messages for a specific user"""
    # Note: This thread is kept minimal since messages are synced via /api/messages endpoint
    # which all clients poll regularly
    while socket_manager.is_connected:
        try:
            # Just keep the connection alive, messages are managed in Flask
            msg = socket_manager.receive_message()
            if msg:
                # Server might send messages, but we primarily use the shared history
                pass
        except Exception as e:
            print(f"Connection thread for user {user_id}: {e}")
            break

@app.route('/')
def index():
    """Render the chat interface"""
    # Generate unique user ID for this session
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return render_template('chat.html', user_id=session['user_id'][:8])

@app.route('/api/connect', methods=['POST'])
def connect():
    """API endpoint to connect to the socket server"""
    user_id = session.get('user_id', str(uuid.uuid4()))
    session['user_id'] = user_id
    
    # Create new socket manager for this user
    socket_manager = SocketManager()
    
    data = request.json
    host = data.get('host', 'localhost')
    port = int(data.get('port', 12345))
    
    success, message = socket_manager.connect_to_server(host, port)
    
    if success:
        user_sockets[user_id] = socket_manager
        # Start receiving messages in background for this user
        threading.Thread(target=receive_messages_thread, args=(user_id, socket_manager), daemon=True).start()
    
    return jsonify({
        'success': success,
        'message': message,
        'isConnected': socket_manager.is_connected,
        'user_id': user_id[:8]
    })

@app.route('/api/send', methods=['POST'])
def send_message():
    """API endpoint to send a message"""
    user_id = session.get('user_id')
    if not user_id or user_id not in user_sockets:
        return jsonify({'success': False, 'message': 'Not connected'}), 400
    
    socket_manager = user_sockets[user_id]
    
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({'success': False, 'message': 'Empty message'}), 400
    
    # Add message to shared history BEFORE sending to socket
    # This ensures all users see it immediately on next poll
    with messages_lock:
        sender_name = f'USER_{user_id[:8]}'
        messages_history.append({
            'user_id': user_id,
            'sender': sender_name,
            'message': message,
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'encryption': 'AES-256'
        })
    
    # Also send through socket for server logging
    success, msg = socket_manager.send_message(message)
    
    return jsonify({
        'success': True,
        'message': 'Message added to history',
        'messages': messages_history
    })

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """API endpoint to get message history"""
    user_id = session.get('user_id')
    is_connected = False
    
    if user_id and user_id in user_sockets:
        is_connected = user_sockets[user_id].is_connected
    
    with messages_lock:
        return jsonify({
            'messages': messages_history,
            'isConnected': is_connected,
            'user_id': user_id[:8] if user_id else None
        })

@app.route('/api/status', methods=['GET'])
def get_status():
    """API endpoint to get connection status"""
    user_id = session.get('user_id')
    is_connected = False
    
    if user_id and user_id in user_sockets:
        is_connected = user_sockets[user_id].is_connected
    
    return jsonify({
        'isConnected': is_connected,
        'user_id': user_id[:8] if user_id else None
    })

@app.route('/api/disconnect', methods=['POST'])
def disconnect():
    """API endpoint to disconnect from server"""
    user_id = session.get('user_id')
    
    if user_id and user_id in user_sockets:
        socket_manager = user_sockets[user_id]
        socket_manager.disconnect()
        del user_sockets[user_id]
    
    return jsonify({
        'success': True,
        'message': 'Disconnected from server',
        'isConnected': False
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

