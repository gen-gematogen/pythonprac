import zlib
import sys
from glob import iglob
from os.path import join

if len(sys.argv) == 1:
    repopath = join(".git", "refs", "heads", "*")
    for i, branch in enumerate(iglob(repopath)):
        print(i + 1, ": ", branch, sep = '')

else:
    repo = sys.argv[1]
    repopath = join(repo, "objects", "??", "*")
    print(repopath)
    for objname in iglob(repopath):
        print(objname)

        with open(objname, "rb") as objfile:
            fullobj = zlib.decompress(objfile.read())
            header, _, body = fullobj.partition(b'\x00')
            kind, size = header.split()
            print(kind.decode(), int(size))#, body)
            if kind == b"commit":
                print(body.decode())
            elif kind == b"tree":
                while body:
                    treehdr, _, tail = body.partition(b'\x00')
                    gitid, body = body[:20], body[20:]
                    print(f"\t{treehdr}, {gitid.hex()}")