import sys
import ipsedixit
import subprocess
import os

if sys.argv[-1] == 'caesar' or sys.argv[-1] == 'tacitus':
    try:
        n = int(sys.argv[-2])
    except:
        n = 4
    generator = ipsedixit.Generator(sys.argv[-1])
elif os.path.isfile(sys.argv[-1]) and len(sys.argv) != 1:
    try:
        n = int(sys.argv[-2])
    except:
        n = 4
    with open(sys.argv[-1], 'r') as f:
        txt = f.read()
    generator = ipsedixit.Generator(txt)
else:
    try:
        n = int(sys.argv[-1])
    except:
        n = 4
    generator = ipsedixit.Generator()

paragraphs = generator.paragraphs(n)
for p in paragraphs:
    print(p)
    print()
