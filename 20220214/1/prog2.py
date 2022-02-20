import zlib
import sys
from glob import iglob
from os.path import join

def printer(commit_id, depth):
    obj_path = join(".git", "objects", commit_id[:2], commit_id[2:])
        
    with open(obj_path, "rb") as f:
        header, _, body = zlib.decompress(f.read()).partition(b'\x00')
            
    kind, size = header.split()
    body = body.decode()

    # Print commit data
    print('-' * depth, ' ', kind.decode(), ' ', int(size), sep = '')
    for s in body.split('\n'):
        print('-' * depth, ' ',s, sep = '')

    tree_id = body.split()[1]
    if body.split()[2] == "parent":
        parent_id = body.split()[3]
    else:
        parent_id = -1

    tree_path = join('.git', 'objects', tree_id[:2], tree_id[2:])
    with open(tree_path, 'rb') as f:
        header, _, body = zlib.decompress(f.read()).partition(b'\x00')

    kind, size = header.split()
       
    print('-' * depth, kind.decode(), int(size))
    while body:
        tree_hdr, _, tail = body.partition(b'\x00')
        attr, _, f_name = tree_hdr.partition(b' ')
        git_id, body = body[:20], body[20:]
        print('-' * depth, f"{f_name.decode()}, {attr.hex()}, {git_id.hex()}")
    print()

    if parent_id != -1:
        printer(parent_id, depth + 1)
    

if len(sys.argv) == 1:
    repopath = join(".git", "refs", "heads", "*")
    for i, branch in enumerate(iglob(repopath)):
        print(i + 1, ": ", branch, sep = '')

else:
    branch = sys.argv[1]
    branch_path = join(".git", "refs", "heads", branch)
    with open(branch_path, "r") as f:
        commit_id = f.read().strip()
        printer(commit_id, 0)
       



    
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
