num = int(input("Enter Number : "))
for i in range(1, num + 1):
 print("*" * i + " " * (2 * (num - i)) + "*" * i)
for j in range(num - 1, 0, -1):
  print("*" * j + " " * (2 * (num - j)) + "*" * j)
