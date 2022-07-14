# exec(open("new_main2.py").read())
from node_thread import node_thread
import time
import socket

out_q = []
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
#self.sock.bind(('0.0.0.0',6454))


def send_q():
    global out_q
    if len(out_q):
        try:
            sock.sendto(out_q[0], ('255.255.255.255', 6454))
            print("sent: "+out_q[0].decode())
            out_q = out_q[1:]
        except Exception as e:
            print("ERROR: Socket error with exception: %s" % e)

custom_thread = node_thread()
custom_thread.task_list.append(send_q)