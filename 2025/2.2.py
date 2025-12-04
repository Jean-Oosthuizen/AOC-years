f = open("2025/input2.txt","r")
ranges = f.readline().strip().split(",")
total = 0

for oneRange in ranges:
  start, end = oneRange.split("-")
  for num in range(int(start), int(end) + 1):
    numStr = str(num)
    numLen = len(numStr)
    for patternLength in range (numLen -1, 0, -1):
      if(numLen % patternLength == 0):
        pattern = numStr[0:patternLength]
        invalidId = True
        for numSegment in range (0, numLen, patternLength):        
          if(numStr[numSegment:numSegment + patternLength] != pattern):
            invalidId = False
            break
        if(invalidId):
          total += num
          break
        

print(total)