import sys
N = int(input())

words = []
for _ in range(N):
  words.append(sys.stdin.readline().rstrip())

# set으로 중복 단어 제거
words_set = list(set(words))

words_with_length = []

for word in words_set:
  words_with_length.append([len(word), word])

sorted_words_with_dic = sorted(words_with_length, key = lambda x: x[1])
sorted_words_with_len = sorted(sorted_words_with_dic, key = lambda x: x[0])

for i in sorted_words_with_len:
  print(i[1])