lst = [7,4,2,1,8,3,6,5]
num = len(lst)

for i in range(num - 1):
  ok = True
  for j in range(num - 1 - i):
    if lst[j] < lst[j+1]:
      lst[j],lst[j+1] = lst[j+1],lst[j]
      ok = False
  if ok:
    break

print("Descending Bubble Sort: ",lst)
