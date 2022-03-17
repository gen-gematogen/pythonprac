import sys
import ast
import re
import textdistance
import difflib

def parse(file):
    with open(file, "r") as f:
        data = ast.parse(f.read())

    pres = ast.dump(data, annotate_fields=False)
    k = 0

    reg = re.findall("[A-Z][A-Za-z]*\(|[,]|[)]", pres)
    for i in range(len(reg)):
        if reg[i][0].isupper():
            reg[i] = chr(ord('a') + k)
            k += 1

    return ''.join(reg), pres

f1, f2 = sys.argv[1:3]

res1, pres1 = parse(f1)
res2, pres2 = parse(f2)

dist = textdistance.damerau_levenshtein.normalized_distance(res1, res2)

if dist <= 0.1:
    print("May be cheating")
    print(difflib.HtmlDiff().make_file(pres1, pres2))
