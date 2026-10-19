num = int(input("Enter Number : "))
for i in range(num):
  for j in range(num):
    print("*" if i == 0 or i == num - 1 or j == 0 or j == num - 1 else " ", end="")
  print()
