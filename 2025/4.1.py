f = open("2025/input4.txt","r")

lines = []
dataHeight = 0
for tempLine in f.readlines():
  dataHeight += 1
  lines.append(tempLine.strip())

dataWidth = len(lines[0])
accessibleRolls = 0

# loop through all positions
for evalx in range(dataWidth):
  for evaly in range(dataHeight):
    if(lines[evaly][evalx] == "@"):
      # evaluate the neighbouring chars of current position 
      neighbourCount = 0
      for y in range(evaly-1, evaly+2): # loop through each neighbour vertically
        if(-1 < y and y < dataHeight):
          for x in range(evalx-1, evalx+2): #loop through each neighbour horizontally
            if(-1 < x and x < dataWidth and (evalx != x or evaly != y)): # if we're not looking at out of bounds or root positions
              if(lines[y][x] == "@"):
                neighbourCount += 1
      if(neighbourCount < 4):
        accessibleRolls += 1
print(accessibleRolls)
