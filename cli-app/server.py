import queue
import os
import signal
import sys
import socket
import subprocess
import threading
import time

MAX_RECV_BYTE = 4096
PORT = 10000

TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM
TRANSPORT_LAYER_PROT = TCP

PIDS = []
SOCKET_ID2PID = {}


def stdout(proc, connection):
    try:
        while proc.poll() is None:
            proc.stdout.flush()
            stdout_text = proc.stdout.readline()

            print(stdout_text, end="")
            connection.send(stdout_text.encode('utf-8'))

    except Exception:
        return


def stdin(proc, connection):
    try:
        while proc.poll() is None:
            # ans = input()
            ans = connection.recv(MAX_RECV_BYTE).decode()
            ans = ans + "\n"
            print(ans)

            proc.stdin.write(ans)
            proc.stdin.flush()

    except Exception:
        return

def run(connection):
    global PIDS

    print("----- Server is running -----")
    p = subprocess.Popen(["python3", "akinator.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')
    print(f"----- Application process id: {p.pid} -----")
    PIDS.append(p.pid)


    t_stdin = threading.Thread(target=stdin, args=(p, connection))
    t_stdout = threading.Thread(target=stdout, args=(p, connection))

    t_stdin.start()
    t_stdout.start()
    t_stdin.join()
    t_stdout.join()


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, TRANSPORT_LAYER_PROT)
    print(f"{socket.gethostname()}:{PORT}")
    s.bind((socket.gethostname(), PORT))
    s.listen(1)

    try:
        while True:
            connection, address = s.accept()
            t = threading.Thread(target=run, args=(connection,))
            t.start()

    finally:
        subprocess.Popen(["sh", "finally.sh"])
