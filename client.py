import socket

def run_client(host='localhost', port=5000):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print(f"Connected to {host}:{port}")
    except Exception as e:
        print(f"Could not connect to the server: {e}")
        return

    while True:
        message = input("Write a message (or 'éxito' to exit):")
        if message.lower() == 'éxito':
            break
        try:
            client.sendall(message.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            print("Server:", response)
        except Exception as e:
            print(f"Error sending/receiving message: {e}")
            break

    client.close()
    print("Disconnected from the server.")

if __name__ == '__main__':
    run_client()