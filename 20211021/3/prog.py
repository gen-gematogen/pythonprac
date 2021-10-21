from collections import defaultdict

word_len = int(input())
s = input()
word_count = defaultdict(lambda: 0)
while s:
    s = ''.join([i for i in s if i.isalpha() or i == ' '])
    print(s)
    s = s.lower().split()
    for word in s:
        if len(word) == word_len:
            word_count[word] += 1
    s = input()
print(*[i[1] for i in sorted(zip(word_count.values(), word_count.keys()))], sep = ' ')