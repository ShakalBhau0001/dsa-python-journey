num = int(input("Enter Number : "))

for i in range(num):
  for j in range(2 * num - 1):
    print("*" if num - 1 - i <= j <= num - 1 + i else " ", end="")
  print()
