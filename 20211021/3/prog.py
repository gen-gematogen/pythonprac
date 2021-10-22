from collections import defaultdict

word_len = int(input())
word_count = defaultdict(lambda: 0)
text = []
while True:
    try:
        s = input()
    except:
        break
    s = ''.join([i if i.isalpha() else ' ' for i in s])
    s = s.lower().split()
    for word in s:
        if len(word) == word_len:
            word_count[word] += 1

max_occ = 0
common_words = []

for k in word_count:
    if word_count[k] > max_occ:
        common_words = [k]
        max_occ = word_count[k]
    elif word_count[k] == max_occ:
        common_words.append(k)
        
if common_words: 
    print(*common_words)