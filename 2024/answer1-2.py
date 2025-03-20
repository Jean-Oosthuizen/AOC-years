f = open("input1.txt","r")
arr1 = []
arr2 = []
for line in f:
  vals = line.strip().split("   ")
  arr1.append(int(vals[0]))
  arr2.append(int(vals[1]))

similarity = 0
for i in range(0,len(arr1)):
  matchCount = 0
  searchVal = arr1[i]
  for j in range(0,len(arr2)):
    if(arr2[j] == searchVal):
      matchCount += 1
  similarity += searchVal * matchCount
print(similarity)