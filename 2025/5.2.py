f = open("2025/input5.txt","r")

firstHalf = True
idRanges = []
for templine in f:
  line = templine.strip()
  if(line != ""):
    minPart, maxPart = list(map(int,line.split("-")))
    for idRange in idRanges:
      # discard current range if its contained by an old range
      if(idRange[0] <= minPart <= idRange[1] and idRange[0] <= maxPart <= idRange[1]):
        minPart = -1
        maxPart = -1
        break
      # discard old range if its contained in current range
      elif(minPart <= idRange[0] <= maxPart and minPart <= idRange[1] <= maxPart):
        idRange[0] = -1
        idRange[1] = -1
      else:
        # adjust minpart to be above closest neighbour range if needed
        if(idRange[0] <= minPart <= idRange[1]):
          minPart = idRange[1] + 1
        # adjust maxpart to be below closest neighbour range if needed
        if(idRange[0] <= maxPart <= idRange[1]):
          maxPart = idRange[0] + -1
    idRanges.append([minPart, maxPart])
      
       
  else:
    break

freshCount = 0

for idRange in idRanges:
  if(idRange[0] != -1):
    freshCount += (idRange[1]-idRange[0])+1
  
print(freshCount)