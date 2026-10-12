# Pattern 1

rows = int(input("Enter Number Of Rows: "))
for j in range(1, rows + 1):
    print("* " * j)

# Pattern 2

rows = int(input("Enter Number Of Rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 3

rows = int(input("Enter Number Of Rows: "))

i = 1
while i <= rows:
    print("* " * i)
    i = i + 1
