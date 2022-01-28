import socket
import threading

MAX_RECV_BYTE = 4096
IP = 'buster'
PORT = 10000
SERVER = (IP, PORT)

TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM
TRANSPORT_LAYER_PROT = TCP

def stdin(sock):
    try:
        while True:
            ans = input()
            sock.send(ans.encode("UTF-8"))

    except Exception:
        return


def stdout(sock):
    try:
        while True:
            text = sock.recv(MAX_RECV_BYTE).decode()
            print(text, end="")

    except Exception:
        return


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, TRANSPORT_LAYER_PROT)
    sock.connect(SERVER)

    try:
        t_stdin = threading.Thread(target=stdin, args=(sock,))
        t_stdout = threading.Thread(target=stdout, args=(sock,))

        t_stdin.start()
        t_stdout.start()

        t_stdin.join()
        t_stdout.join()


    finally:
        sock.close()
