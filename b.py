n, k = list(map(int, input().split()))
flags = [False] * n
count = 0

for i in range(k):
  d = int(input())
  people = list(map(int, input().split()))
  for p in people:
    flags[p - 1] = True
for flag in flags:
  if not flag:
    count += 1
print(count)
