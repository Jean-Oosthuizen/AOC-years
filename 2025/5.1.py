f = open("2025/input5.txt","r")

firstHalf = True
idRanges = []
ids = []
for templine in f:
  line = templine.strip()
  if(line != ""):
    if(firstHalf):
      idRanges.append(list(map(int, line.split("-"))))
    else:
      ids.append(int(line))
  else:
    firstHalf = False

freshCount = 0
for iid in ids:
  for idRange in idRanges:
    if(idRange[0] <= iid and iid <= idRange[1]):
      freshCount += 1
      break
print(freshCount)