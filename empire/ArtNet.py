import socket

class ArtNet:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        try:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except Exception as e:
            print("REUSEADDR, did not work for OSX after binding other apps could not use the port:")
            print(e)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.REUSEADDR, 1)

    def update(self):
        if len(self.out_q):
        try:
            sock.sendto(self.out_q[0], ('255.255.255.255', 6454))
            print("sent: "+self.out_q[0].decode())
            self.out_q = self.out_q[1:]
        except Exception as e:
            print("ERROR: Socket error with exception: %s" % e)

    def generate_header(self, op_code):
        '''
        Generates artnet packet header with correct op_code
        '''
        header = bytearray()
        header.extend(bytearray('Art-Net', 'utf8'))
        header.append(0x0)
        
        header.append(op_code.to_bytes(2,'little'))
        header.append(0x0) # Protocol version High
        header.append(0x0) # Protocol version low
        header.append(0x0) # Sequence 1-255 to enable and keep in order
        header.append(0x0) # Physical universe
        header.append(0x1.to_bytes(2,'little')) # Universe (little endian)
        header.append(0x0) # Lenght high 
        header.append(0x0) # Lenght Low # only even number from 2-512
        return header
