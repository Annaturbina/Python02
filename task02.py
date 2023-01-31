s = int(input())
p = int(input())
for x in range(1000):
  for y in range(1000):
    if (x + y == s) and (x * y == p):
      if x <= y:
        print(x, y)