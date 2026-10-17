num = int(input("Enter Number : "))

for i in range(num):
  for j in range(num):
    print("*" if j < num - i else " ", end="")
  print()
