# encoding: utf-8 # for sending , receiving zh-cn

import socket

if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(("127.0.0.1",8080))

    #msg = bytearray()
    #msg.extend(bytearray("@appl=I want an apple(我想要一个苹果)", 'UTF-8'))
    msg = "@appl=I want an apple(我想要一个苹果)"
    sock.sendall(msg)

    while True:
        data = sock.recv(1024)

        if data:
            head = data[:5]
            body = data[6:]
            if head == "@prog": #mesg recv sequence depends on server
                print body
            if head == "@appl":
                print "client got return message:"+str(body)

    s.close()

