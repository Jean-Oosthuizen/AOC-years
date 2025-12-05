f = open("2025/input4.txt","r")

lines = []
dataHeight = 0
for tempLine in f.readlines():
  dataHeight += 1
  lines.append(list(tempLine.strip()))

dataWidth = len(lines[0])

anyRollsRemovable = True
removedRolls = 0

while anyRollsRemovable:
  accessibleRolls = 0
  # loop through all positions, marking removables
  for evaly in range(dataHeight):
    for evalx in range(dataWidth):
      if(lines[evaly][evalx] == "@"):
        # evaluate the neighbouring chars of current position 
        neighbourCount = 0
        for y in range(evaly-1, evaly+2): # loop through each neighbour vertically
          if(-1 < y and y < dataHeight):
            for x in range(evalx-1, evalx+2): #loop through each neighbour horizontally
              if(-1 < x and x < dataWidth and (evalx != x or evaly != y)): # if we're not looking at out of bounds or root positions
                if(lines[y][x] == "@" or lines[y][x] == "X"):
                  neighbourCount += 1
        if(neighbourCount < 4):
          lines[evaly][evalx] = "X"
          accessibleRolls += 1
    
  if accessibleRolls > 0:
    for y in range(dataHeight):
      for x in range(dataWidth):
        if(lines[y][x] == "X"):
          removedRolls += 1
          lines[y][x] = "."
  else:
    anyRollsRemovable = False
    
print(removedRolls)
