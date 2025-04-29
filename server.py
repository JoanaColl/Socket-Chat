import socket
import sqlite3
from datetime import datetime

# Configuración del socket TCP/IP
def init_socket(host='localhost', port=5000):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        print(f"Server listening on {host}:{port}")
        return server
    except OSError as e:
        print(f"Failed to initialize host: {e}")
        exit(1)

# Inicialización y verificación de la base de datos
def init_db(name_db="messages.db"):
    try:
        conn = sqlite3.connect(name_db)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                shipping_date TEXT NOT NULL,
                client_ip TEXT NOT NULL
            )
        ''')
        conn.commit()
        return conn
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
        exit(1)

# Guardar mensaje en la base de datos
def save_messages(conn, content, shipping_date, client_ip):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (content, shipping_date, client_ip) VALUES (?, ?, ?)",
                       (content, shipping_date, client_ip))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error saving message: {e}")

# Manejo de cada cliente
def handle_client(client_socket, address, conn_db):
    client_ip = address[0]
    print(f"Connection established with {client_ip}")
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_messages(conn_db, data, timestamp, client_ip)
            response = f"Message received: {timestamp}"
            client_socket.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"Error connecting with {client_ip}: {e}")
            break
    client_socket.close()
    print(f"Connection closed with {client_ip}")

# Ciclo principal del servidor
def run_server():
    server = init_socket()
    conn_db = init_db()
    while True:
        client_socket, address = server.accept()
        handle_client(client_socket, address, conn_db)

if __name__ == '__main__':
    run_server()