import textdistance
from multiprocessing import Pool

def dist(s1, s2, s3):
    if s3 == "L":
        return textdistance.Levenshtein(s1, s2)
    elif s3 == "D":
        return textdistance.damerau_levenstein(s1, s2)
    return -1
    
s = input()
s1, s2 = s.split()[:2]
s3 = input()

with Pool(1) as p:
    res = p.map(dist, [(s1, s2, s3)])
    print(res)
