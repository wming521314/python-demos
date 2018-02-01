# coding: utf-8

# a = b'\xde\xad\xbe\xef'
# 这种形式是python中的bytes的定义方法,跟nodejs,c有所不同

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

    b = u'你好'
    b1 = bytearray(b, encoding='utf-8')

    print(b) #你好
    print(len(b)) #2
    print(b1) #你好
    print(len(b1)) #6
    print(binascii.hexlify(b1)) #e4bda0e5a5bd



