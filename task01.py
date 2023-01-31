n = int(input())
string_coins = input()
coins = string_coins.split()
count_heads = 0
count_tails = 0
for i in range(0, len(coins), 1):
  if coins[i] == "1":
    count_heads += 1
  else:
    count_tails += 1
if count_tails <= count_heads:
  print(count_tails)
else:
  print(count_heads)