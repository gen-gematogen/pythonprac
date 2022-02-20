import zlib
import sys
from glob import iglob
from os.path import join

if len(sys.argv) == 1:
    repopath = join(".git", "refs", "heads", "*")
    for i, branch in enumerate(iglob(repopath)):
        print(i + 1, ": ", branch, sep = '')

else:
    branch = sys.argv[1]
    branch_path = join(".git", "refs", "heads", branch)
    with open(branch_path, "r") as f:
        commit_id = f.read().strip()
        obj_path = join(".git", "objects", commit_id[:2], commit_id[2:])
        
        with open(obj_path, "rb") as f:
            header, _, body = zlib.decompress(f.read()).partition(b'\x00')
            
        kind, size = header.split()

        if kind == b"commit":
            print(kind.decode(), ' ', int(size), '\n', body.decode(), sep = '')
    
#    for objname in iglob(repopath):
#        print(objname)
#
#        with open(objname, "rb") as objfile:
#            fullobj = zlib.decompress(objfile.read())
#            header, _, body = fullobj.partition(b'\x00')
#            kind, size = header.split()
#            print(kind.decode(), int(size))#, body)
#            if kind == b"commit":
#                print(body.decode())
#            elif kind == b"tree":
#                while body:
#                    treehdr, _, tail = body.partition(b'\x00')
#                    gitid, body = body[:20], body[20:]
#                    print(f"\t{treehdr}, {gitid.hex()}")
