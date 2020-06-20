def calc(a, b):
  return a ** 5 - b ** 5

x = int(input())
even = 0
if x % 2 == 0:
  even = 1
flag = 0
if even:
  a = 2
else:
  a = 1
b = 0
while (True):
  while (True):
    if calc(a,b) == x:
      flag = 1
      break
    elif calc(a,b) > x:
      break
    b -= 2
  if flag == 1:
    break
  a += 1
  if even:
    b = a - 2
  else:
    b = a - 1
print(a, b)
      
