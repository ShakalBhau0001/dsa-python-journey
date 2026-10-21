num = int(input("Enter Number : "))
for i in range(num):
  print(" " * i + "*" * (2 * (num - i) - 1))
for j in range(1, num):
  print(" " * (num - j - 1) + "*" * (2 * j + 1))
