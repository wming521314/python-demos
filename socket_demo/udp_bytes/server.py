from socket import *
import binascii

HOST = '127.0.0.1'
PORT = 5000

if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print '...waiting for message..'
    while True:
        data, address = sock.recvfrom(24)
        print(address) # ('127.0.0.1', 35550)
        print(type(data)) # <type 'str'>
        print(len(data)) # 24 12
        print(data) # xxxxx hello server
        print(binascii.hexlify(data)) #00c029e9785991b13173a11a30ebbe198a61f5292e4ca433 68656c6c6f20736572766572
    sock.close()