num = int(input("Enter Number : "))

for i in range(num):
  for j in range(num):
    print("*" if j >= i else " ", end="")
  print()
