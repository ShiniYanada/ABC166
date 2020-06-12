n, m = list(map(int, input().split()))
heights = list(map(int, input().split()))
flags = [True] * n
count = 0
for _ in range(m):
  roots = list(map(int, input().split()))
  if heights[roots[0] - 1] > heights[roots[1] - 1]:
    flags[roots[1] - 1] = False
  elif heights[roots[0] - 1] < heights[roots[1] - 1]:
    flags[roots[0] - 1] = False
  else:
    flags[roots[1] - 1] = False
    flags[roots[0] - 1] = False
for flag in flags:
  if flag:
    count += 1
