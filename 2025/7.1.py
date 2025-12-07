f = open("2025/input7.txt", "r")

rows = []
for line in f:
  rows.append(line.strip())
dataWidth = len(rows[0])
dataHeight = len(rows)

laserIndexes = []
output = 0

for y in range(dataHeight):
  newLaserIndexes = []
  for x in range(dataWidth):
    if(rows[y][x] == "S"):
      # laser start
      newLaserIndexes.append(x)
    elif(x in laserIndexes):
      if(rows[y][x] == "^"):
        # add lasers to each side of the splitter
        newLaserIndexes.extend([x-1,x+1])
        output += 1
      else:
        # allow laser to continue straight
        newLaserIndexes.append(x)
  laserIndexes = newLaserIndexes
print(output)
