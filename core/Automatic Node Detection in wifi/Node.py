import socket
import threading

PORT = 5001
peers = []  # list of discovered peers


# =========================
# Server part
# =========================
def handle_client(conn, addr):
    """Handles incoming client connections."""
    print(f"[+] Incoming connection from {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"[{addr}] {data}")
            # Send acknowledgment back to the sender
            response = f"ACK: {data}"
            conn.sendall(response.encode())
        except:
            break
    conn.close()
    print(f"[-] Connection closed: {addr}")


def start_server():
    """Starts a TCP server to listen for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', PORT))  # listen on all interfaces
    server_socket.listen(5)

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Node running on {local_ip}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()


# =========================
# Client part
# =========================
def discover_peers():
    """Scans the local subnet for peers running the server."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        subnet = '.'.join(local_ip.split('.')[:-1]) + '.'
        print(f"[*] Scanning subnet: {subnet}0/24")
    finally:
        s.close()

    found = []
    for i in range(1, 255):
        ip = subnet + str(i)
        try:
            test_socket = socket.create_connection((ip, PORT), timeout=0.05)
            found.append(ip)
            print(f"[+] Found peer: {ip}:{PORT}")
            test_socket.close()
        except:
            continue
    return found


def send_message(target_ip):
    """Connects to a peer and allows sending messages."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, PORT))
        print(f"[+] Connected to {target_ip}:{PORT}")

        while True:
            msg = input("Enter message (or 'exit' to disconnect): ")
            if msg.lower() == 'exit':
                break
            client_socket.sendall(msg.encode())
            response = client_socket.recv(1024).decode()
            print(f"[{target_ip}] {response}")

        client_socket.close()
    except Exception as e:
        print(f"[-] Failed to connect: {e}")

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()

    peers = discover_peers()
    print("\nDiscovered peers:")
    for idx, peer in enumerate(peers):
        print(f"{idx+1}. {peer}")

    while True:
        if not peers:
            print("[-] No peers found. Rescanning...")
            peers = discover_peers()
            continue

        try:
            choice = int(input("\nSelect peer number to connect (0 to rescan): "))
            if choice == 0:
                peers = discover_peers()
                continue
            target = peers[choice - 1]
            send_message(target)
        except Exception as e:
            print(f"[!] Invalid choice or error: {e}")