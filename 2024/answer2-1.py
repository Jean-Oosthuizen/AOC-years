f = open("input2.txt","r")
reports = []
for line in f:
  reports.append(line.strip().split(" "))
safeCount = 0

for report in reports:
  
  safe = True
  if(int(report[0]) < int(report[1])):
    ascending = True
  else:
    ascending = False
  
  for i in range(0,len(report) - 1):
    level1 = int(report[i])
    level2 = int(report[i+1])
    difference = abs(level1-level2)
    if(difference < 1 or difference > 3):
      safe = False
    else:
      if(ascending and level1 > level2):
        safe = False
      elif(not ascending and level1 < level2):
        safe = False
  if(safe):
    safeCount += 1

print(safeCount)
      
