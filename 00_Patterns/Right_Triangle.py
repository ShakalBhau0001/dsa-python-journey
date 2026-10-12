# Pattern 1

rows = int(input("Enter Number Of Rows: "))

for i in range(1, rows + 1):
    print("  " * (rows - i) + "* " * i)


# Pattern 2

rows = int(input("Enter Number Of Rows: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# Pattern 3

rows = int(input("Enter Number Of Rows: "))

i = 1
while i <= rows:
    print("  " * (rows - i) + "* " * i)
    i = i + 1
