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
