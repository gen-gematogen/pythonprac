import textdistance

def dist(s1, s2, s3):
    if s3 == "L":
        return textdistance.Levenshtein(s1, s2)
    elif s3 == "D":
        return textdistance.damerau_levenstein(s1, s2)
    return -1
    
s = input()
s1, s2 = s.split()[:2]
s3 = input()

res = dist(s1, s2, s3)
