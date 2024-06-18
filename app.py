from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Ensure database path is correct
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visitors.db')

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT,
            visit_time TEXT,
            referrer TEXT,
            user_agent TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/log_visit', methods=['POST'])
def log_visit():
    data = request.json
    ip_address = request.remote_addr
    visit_time = data.get('visit_time')
    referrer = data.get('referrer')
    user_agent = request.headers.get('User-Agent')
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO visitors (ip_address, visit_time, referrer, user_agent)
        VALUES (?, ?, ?, ?)
    ''', (ip_address, visit_time, referrer, user_agent))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
