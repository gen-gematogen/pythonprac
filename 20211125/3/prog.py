import struct
import sys

data = sys.stdin.buffer.read()

try:
    form = ['4s', 'i', '4s', '3s', 'h', 'h', 'i', 'h', '4s', 'i']
    shift = [0, 4, 8, 12, 20, 22, 24, 34, 36, 40]
    extracted_data = [struct.unpack_from(f, data, s)[0] for f, s in zip(form, shift)]

    if extracted_data[0] != b"RIFF" or extracted_data[2] != b"WAVE" or extracted_data[3] != b"fmt" or extracted_data[-2] != b"data":
        raise Exception
except:
    print("NO")
else:
    print(f'Size={extracted_data[1]}, Type={extracted_data[4]}, Channels={extracted_data[5]}, Rate={extracted_data[6]}, Bits={extracted_data[7]}, Data size={extracted_data[-1]}')

