num = int(input("Enter Number : "))

for i in range(num):
  for j in range(2 * num - 1):
    print("*" if i <= j <= 2 * num - 2 - i else " ", end="")
  print()
