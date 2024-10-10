import sys
N = int(input())

people = []

for n in range(N):
    old, name = map(str, sys.stdin.readline().split())
    people.append((int(old), name))

old_sorted = sorted(people, key=lambda x: (x[0]))

for p in old_sorted:
    print(p[0], p[1])