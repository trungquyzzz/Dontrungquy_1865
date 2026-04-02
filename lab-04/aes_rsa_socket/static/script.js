// ========================================
// SECURE CHAT - JavaScript Logic
// AES-RSA Encrypted Communication Client
// ========================================

class SecureChatApp {
    constructor() {
        this.isConnected = false;
        this.messagesSent = 0;
        this.messagesReceived = 0;
        this.sessionStartTime = null;
        this.messageUpdateInterval = null;
        this.userId = null;
        this.lastMessageCount = 0;

        this.initializeElements();
        this.attachEventListeners();
    }

    initializeElements() {
        // Connection elements
        this.serverHostInput = document.getElementById('server-host');
        this.serverPortInput = document.getElementById('server-port');
        this.connectBtn = document.getElementById('connect-btn');
        this.disconnectBtn = document.getElementById('disconnect-btn');

        // Status elements
        this.statusIndicator = document.getElementById('status-indicator');
        this.encryptionInfo = document.getElementById('encryption-info');
        this.encryptionStatus = document.getElementById('encryption-status');

        // Chat elements
        this.messagesContainer = document.getElementById('messages-container');
        this.messageInput = document.getElementById('message-input');
        this.sendBtn = document.getElementById('send-btn');

        // Info elements
        this.msgsSentCount = document.getElementById('msgs-sent');
        this.msgsReceivedCount = document.getElementById('msgs-received');
        this.sessionDuration = document.getElementById('session-duration');
    }

    attachEventListeners() {
        this.connectBtn.addEventListener('click', () => this.connect());
        this.disconnectBtn.addEventListener('click', () => this.disconnect());
        this.sendBtn.addEventListener('click', () => this.sendMessage());

        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey && this.isConnected) {
                this.sendMessage();
            }
        });
    }

    async connect() {
        this.connectBtn.disabled = true;
        this.addSystemMessage('Connecting to server...');

        try {
            const host = this.serverHostInput.value || 'localhost';
            const port = this.serverPortInput.value || '12345';

            const response = await fetch('/api/connect', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    host: host,
                    port: port
                })
            });

            const data = await response.json();

            if (data.success) {
                this.isConnected = true;
                this.userId = data.user_id;
                this.sessionStartTime = new Date();

                // Update UI
                this.updateConnectionStatus(true);
                this.addSystemMessage(`✓ Connected as User [${this.userId}] to ${host}:${port}\n🔐 AES-256 encryption active\n🔑 RSA-2048 key exchange complete`);
                this.messageInput.disabled = false;
                this.sendBtn.disabled = false;
                this.connectBtn.disabled = true;
                this.disconnectBtn.disabled = false;

                // Start polling for messages
                this.startMessagePolling();

                // Start session duration timer
                this.startSessionTimer();

                this.updateEncryptionStatus(true);
            } else {
                this.addSystemMessage(`✗ Connection failed: ${data.message}`);
                this.connectBtn.disabled = false;
            }
        } catch (error) {
            this.addSystemMessage(`✗ Error: ${error.message}`);
            this.connectBtn.disabled = false;
        }
    }

    async disconnect() {
        try {
            await fetch('/api/disconnect', {
                method: 'POST'
            });

            this.isConnected = false;
            this.updateConnectionStatus(false);
            this.addSystemMessage('Disconnected from server');

            // Reset UI
            this.messageInput.disabled = true;
            this.sendBtn.disabled = true;
            this.connectBtn.disabled = false;
            this.disconnectBtn.disabled = true;

            // Stop polling
            if (this.messageUpdateInterval) {
                clearInterval(this.messageUpdateInterval);
            }

            this.updateEncryptionStatus(false);
        } catch (error) {
            this.addSystemMessage(`Error disconnecting: ${error.message}`);
        }
    }

    async sendMessage() {
        const message = this.messageInput.value.trim();

        if (!message) {
            this.addSystemMessage('Cannot send empty message');
            return;
        }

        if (!this.isConnected) {
            this.addSystemMessage('Not connected to server');
            return;
        }

        try {
            const response = await fetch('/api/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message
                })
            });

            const data = await response.json();

            if (data.success) {
                this.messageInput.value = '';
                this.messagesSent++;
                this.msgsSentCount.textContent = this.messagesSent;
                // Display message immediately (will be fetched again from server but that's ok)
                this.addUserMessage(message, this.getTimestamp(), 'AES-256');
                this.updateEncryptionStatus(true);
            } else {
                this.addSystemMessage(`Send failed: ${data.message}`);
            }
        } catch (error) {
            this.addSystemMessage(`Error sending message: ${error.message}`);
        }
    }

    startMessagePolling() {
        // Poll for new messages every 500ms
        this.messageUpdateInterval = setInterval(() => {
            this.fetchMessages();
        }, 500);
    }

    async fetchMessages() {
        try {
            const response = await fetch('/api/messages');
            const data = await response.json();

            // Count messages from other users (not from current user)
            const currentUserSender = `USER_${this.userId}`;
            const otherUserMsgs = data.messages.filter(msg => msg.sender !== currentUserSender);
            this.msgsReceivedCount.textContent = otherUserMsgs.length;
            this.messagesReceived = otherUserMsgs.length;

            // Display new messages
            this.displayMessages(data.messages);
        } catch (error) {
            console.error('Error fetching messages:', error);
        }
    }

    displayMessages(messages) {
        // Only add messages starting from last count
        if (messages.length > this.lastMessageCount) {
            const newMessages = messages.slice(this.lastMessageCount);
            const currentUserSender = `USER_${this.userId}`;

            newMessages.forEach(msg => {
                if (msg.sender === currentUserSender) {
                    // Own message - display as YOU
                    this.addUserMessage(msg.message, msg.timestamp, msg.encryption);
                } else if (msg.sender.startsWith('USER_')) {
                    // Other user's message
                    this.addOtherUserMessage(msg.sender, msg.message, msg.timestamp, msg.encryption);
                } else if (msg.sender === 'SYSTEM') {
                    // Skip system messages already shown
                } else {
                    this.addServerMessage(msg.message, msg.timestamp, msg.encryption);
                }
            });
            this.lastMessageCount = messages.length;
        }
    }

    addOtherUserMessage(sender, message, timestamp, encryption) {
        const messageEl = document.createElement('div');
        messageEl.className = 'message received';
        messageEl.innerHTML = `
            <div class="message-header">
                <span class="sender">${sender}</span>
                <div style="display: flex; gap: 8px;">
                    <span class="timestamp">[${timestamp}]</span>
                    <span class="encryption-label">${encryption || 'AES-256'}</span>
                </div>
            </div>
            <div class="message-text">${this.escapeHtml(message)}</div>
        `;
        this.messagesContainer.appendChild(messageEl);
        this.scrollToBottom();
    }

    addUserMessage(message, timestamp, encryption) {
        const time = timestamp || this.getTimestamp();
        const messageEl = document.createElement('div');
        messageEl.className = 'message sent';
        messageEl.innerHTML = `
            <div class="message-header">
                <span class="sender">YOU</span>
                <div style="display: flex; gap: 8px;">
                    <span class="timestamp">[${time}]</span>
                    <span class="encryption-label">${encryption || 'AES-256'}</span>
                </div>
            </div>
            <div class="message-text">${this.escapeHtml(message)}</div>
        `;
        this.messagesContainer.appendChild(messageEl);
        this.scrollToBottom();
    }

    addServerMessage(message, timestamp, encryption) {
        const time = timestamp || this.getTimestamp();
        const messageEl = document.createElement('div');
        messageEl.className = 'message received';
        messageEl.innerHTML = `
            <div class="message-header">
                <span class="sender">SERVER</span>
                <div style="display: flex; gap: 8px;">
                    <span class="timestamp">[${time}]</span>
                    <span class="encryption-label">${encryption || 'AES-256'}</span>
                </div>
            </div>
            <div class="message-text">${this.escapeHtml(message)}</div>
        `;
        this.messagesContainer.appendChild(messageEl);
        this.scrollToBottom();
    }

    addSystemMessage(message) {
        const timestamp = this.getTimestamp();
        const messageEl = document.createElement('div');
        messageEl.className = 'system-message';
        messageEl.innerHTML = `
            <span class="timestamp">[${timestamp}]</span>
            <span class="message-text">${this.escapeHtml(message)}</span>
        `;
        this.messagesContainer.appendChild(messageEl);
        this.scrollToBottom();
    }

    scrollToBottom() {
        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }

    updateConnectionStatus(connected) {
        if (connected) {
            this.statusIndicator.classList.remove('offline');
            this.statusIndicator.classList.add('online');
            this.statusIndicator.innerHTML = `
                <span class="dot"></span> ONLINE
            `;
        } else {
            this.statusIndicator.classList.remove('online');
            this.statusIndicator.classList.add('offline');
            this.statusIndicator.innerHTML = `
                <span class="dot"></span> OFFLINE
            `;
        }
    }

    updateEncryptionStatus(active) {
        if (active) {
            this.encryptionInfo.textContent = 'ENCRYPTION: ACTIVE';
            this.encryptionInfo.style.color = '#00ff41';
            this.encryptionInfo.style.borderColor = '#00ff41';
            this.encryptionStatus.textContent = '🔒 Encryption active - Secure communication established';
            this.encryptionStatus.className = 'status-text success';
        } else {
            this.encryptionInfo.textContent = 'ENCRYPTION: DISABLED';
            this.encryptionInfo.style.color = '#ff006e';
            this.encryptionInfo.style.borderColor = '#ff006e';
            this.encryptionStatus.textContent = '🔓 Not encrypted - Awaiting secure connection';
            this.encryptionStatus.className = 'status-text error';
        }
    }

    startSessionTimer() {
        setInterval(() => {
            if (this.isConnected && this.sessionStartTime) {
                const now = new Date();
                const diff = now - this.sessionStartTime;

                const hours = Math.floor(diff / 3600000);
                const minutes = Math.floor((diff % 3600000) / 60000);
                const seconds = Math.floor((diff % 60000) / 1000);

                const formattedTime = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
                this.sessionDuration.textContent = formattedTime;
            }
        }, 1000);
    }

    getTimestamp() {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        return `${hours}:${minutes}:${seconds}`;
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize the chat app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.chatApp = new SecureChatApp();

    // Add welcome message
    window.chatApp.addSystemMessage(
        '🔐 SECURE CHAT INITIALIZED\n' +
        '━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n' +
        'Encoding: AES-256 CBC\n' +
        'Key Exchange: RSA-2048 OAEP\n' +
        'Status: Ready for connection\n\n' +
        'Step 1: Configure server host and port\n' +
        'Step 2: Click CONNECT to establish secure channel\n' +
        'Step 3: Begin encrypted communication'
    );
});
