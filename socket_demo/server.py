# encoding: utf-8

import socket
import time

if __name__ == "__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(("127.0.0.1",8080))
    sk.listen(5)

    conn,addr = sk.accept()
    print "connected by ", addr

    while True:
        data = conn.recv(1024)
        if data:
            if data:
                head = data[:5]
                body = data[6:]
                if(head=="@appl"):
                    print "server has got client message:"+str(body)
                    for i in range(100):
                        conn.sendall("@prog=Loading %d..."%i)
                        time.sleep(0.2)
                    conn.sendall("@appl=A big big big apple")
        #print "server got arequest , message sent"
    conn.close()

