f = open("input2.txt","r")
reports = []
for line in f:
  reports.append(line.strip().split(" "))
safeCount = 0
for report in reports:
  safe = False
  # loop through twice, under the assumption it's either ascending or descending
  for j in range(0,2):
    if(j == 0):
      ascending = True
    else:
      ascending = False

    #loop through levels
    for i in range(0, len(report)):
      loopSafe = True
      reportCopy = report.copy()
      reportCopy.pop(i)
      for k in range(0, len(reportCopy) - 1):
        level1 = int(reportCopy[k])
        level2 = int(reportCopy[k+1])
        difference = abs(level1-level2)

        if(difference < 1 or difference > 3):
          loopSafe = False
          break
        elif(ascending and level1 > level2):
          loopSafe = False
          break
        elif(not ascending and level1 < level2):
          loopSafe = False
          break
      if(loopSafe):
        safe = True
        break
    if(safe):
      break
  if(safe):
    safeCount += 1
    
print(safeCount)
      
