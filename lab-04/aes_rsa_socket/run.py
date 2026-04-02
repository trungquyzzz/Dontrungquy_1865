"""
Run the complete Secure Chat application
Starts both the socket server and the Flask web server
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def run_secure_chat():
    # Get the current directory
    current_dir = Path(__file__).parent
    
    print("=" * 60)
    print("🔐 SECURE CHAT - AES-RSA Encrypted Communication")
    print("=" * 60)
    print()
    
    # Check if requirements are installed
    print("[1/3] Checking dependencies...")
    try:
        import flask
        from Crypto.Cipher import AES
        print("✓ Dependencies are installed")
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("\nInstalling requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      cwd=current_dir)
    
    print()
    print("[2/3] Starting Socket Server...")
    print("  Host: localhost:12345")
    
    # Start the socket server in background
    server_process = subprocess.Popen(
        [sys.executable, "server.py"],
        cwd=current_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    time.sleep(2)  # Wait for server to start
    
    if server_process.poll() is None:
        print("✓ Socket Server started")
    else:
        print("✗ Failed to start Socket Server")
        print("  Make sure you don't have another instance running on port 12345")
        return
    
    print()
    print("[3/3] Starting Flask Web Server...")
    print("  URL: http://localhost:5000")
    print()
    print("=" * 60)
    print("🟢 SECURE CHAT is running!")
    print("=" * 60)
    print()
    print("📱 Open your browser and go to: http://localhost:5000")
    print()
    print("Press Ctrl+C to stop all services")
    print()
    
    try:
        # Start the Flask web server (runs in foreground)
        subprocess.run(
            [sys.executable, "web_server.py"],
            cwd=current_dir
        )
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        server_process.terminate()
        server_process.wait(timeout=5)
        print("✓ All services stopped")
        sys.exit(0)

if __name__ == "__main__":
    run_secure_chat()
