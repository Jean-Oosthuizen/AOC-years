f = open("input1.txt","r")
arr1 = []
arr2 = []
for line in f:
  vals = line.strip().split("   ")
  arr1.append(vals[0])
  arr2.append(vals[1])
arr1.sort()
arr2.sort()

tally = 0
for i in range(0,len(arr1)):
  tally += abs(int(arr1[i]) - int(arr2[i]))
print(tally)