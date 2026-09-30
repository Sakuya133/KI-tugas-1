importhreading
from getpass import getpass socket
import t

from des import encrypt_message, decrypt_message


PORT = 5000
MAX_PACKET_SIZE = 1_000_000


def receive_exact(sock, size):
    data = b""

    while len(data) < size:
        chunk = sock.recv(size - len(data))

        if not chunk:
            raise ConnectionError("Lawan chat disconect")

        data += chunk

    return data


def send_packet(sock, data):
    packet_length = len(data).to_bytes(4, "big")
    sock.sendall(packet_length + data)


def receive_packet(sock):
    packet_length = int.from_bytes(receive_exact(sock, 4), "big")

    if packet_length < 16 or packet_length > MAX_PACKET_SIZE:
        raise ValueError("Ukuran paket tidak valid")

    return receive_exact(sock, packet_length)


def receive_messages(sock, key):
    while True:
        try:
            packet = receive_packet(sock)

            iv = packet[:8]
            ciphertext = packet[8:]

            message = decrypt_message(iv, ciphertext, key)
            print(f"\nLawan: {message.decode('utf-8')}")
            print("> ", end="", flush=True)

        except (ConnectionError, OSError):
            print("\nKoneksi terputus.")
            break
        except (ValueError, UnicodeDecodeError) as error:
            print(f"\nPesan tidak bisa dibaca: {error}")
            break


def chat(sock, key):
    receiver = threading.Thread(
        target=receive_messages,
        args=(sock, key),
        daemon=True
    )
    receiver.start()

    try:
        while receiver.is_alive():
            message = input("> ")

            if message == "/keluar":
                break

            if not message:
                continue

            iv, ciphertext = encrypt_message(message.encode("utf-8"), key)

            send_packet(sock, iv + ciphertext)

            print(f"Terkirim (ciphertext): {ciphertext.hex()}")

    except (KeyboardInterrupt, EOFError):
        pass
    except (ConnectionError, OSError) as error:
        print(f"\nGagal mengirim: {error}")
    finally:
        sock.close()


def main():
    mode = input("[server/client]: ").strip().lower()


    key_hex = getpass("key DES (16 karakter hex): ").strip()

    try:
        key = bytes.fromhex(key_hex)

        if len(key) != 8:
            raise ValueError()

    except ValueError:
        print("Key 16 karakter hex (8 byte).")
        return

    if mode == "server":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(("0.0.0.0", PORT))
            server.listen(1)

            print(f"\nMenunggu client pada port {PORT}...")
            sock, address = server.accept()
            print(f"Terhubung dengan {address[0]}:{address[1]}")

            chat(sock, key)

    else:
        server_ip = input("IP pc server: ").strip()

        try:
            sock = socket.create_connection((server_ip, PORT), timeout=10)
            sock.settimeout(None)
            chat(sock, key)



if __name__ == "__main__":
    main()