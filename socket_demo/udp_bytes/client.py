# coding: utf-8
from socket import *
import binascii

HOST = '127.0.0.1'
PORT = 5000

if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.connect((HOST, PORT))
    data_buf = bytes(b'\x00\xc0\x29\xe9\x78\x59\x91\xb1\x31\x73\xa1\x1a\x30\xeb\xbe\x19\x8a\x61\xf5\x29\x2e\x4c\xa4\x33')
    # print(binascii.hexlify(message)) #00c029e9785991b13173a11a30ebbe198a61f5292e4ca433
    msg = b"hello server"

    sock.sendto(data_buf, (HOST, PORT))
    sock.sendto(msg, (HOST, PORT))
    sock.close()
