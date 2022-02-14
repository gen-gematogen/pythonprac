import zlib
import sys

with open(sys.argv[1], "rb") as objfile:
    print(zlib.decompress(objfile.read()))
