import textdistance

def dist(s1, s2):
    return textdistance.Levenshtein(s1, s2)

s = input()
s1, s2 = s.split()[:2]

res = dist(s1, s2)
