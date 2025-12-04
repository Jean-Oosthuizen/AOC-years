f = open("input2.txt","r")
ranges = f.readline().strip().split(",")
total = 0

for oneRange in ranges:
  start, end = oneRange.split("-")
  for i in range(int(start), int(end) + 1):
    stri = str(i)
    numLen = len(stri)
    if(numLen % 2 == 0):
      firstHalf = stri[0:numLen//2]
      secondHalf = stri[numLen//2:numLen]

      if(firstHalf == secondHalf):
        total += i

print(total)