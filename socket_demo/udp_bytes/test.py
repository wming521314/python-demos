# coding: utf-8
from socket import *
import binascii

if __name__ == "__main__":

    a = b'\xde\xad\xbe\xef'
    a_bytes = bytes(a)
    a_bytearray = bytearray(a)

    print(a)
    print(a_bytes)
    print(a_bytearray) #4
    print(binascii.hexlify(a)) #deadbeef

    print(len(a)) #4
    print(len(a_bytes)) #4
    print(len(a_bytearray)) #4

    '''
    c = bytearray()
    # d =
    a = bytes(b'haah')
    b = bytes("你好")
    print len(a)
    print len(b)
    print b
    print c
    print len(c)
    '''
