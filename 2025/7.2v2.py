from functools import lru_cache, cache
import time

start = time.time()

f = open("2025/input7.txt", "r")
rows = []
for line in f:
  rows.append(line.strip())
f.close()
dataWidth = len(rows[0])
dataHeight = len(rows)

#calculatedBranches = {}

@lru_cache(maxsize=1024)
def laserPath(y, x):
  if(y == dataHeight-1):
    # base case, end of path
    return 1
  #elif((y,x) in calculatedBranches):
    # use the previously calculated number of paths from this splitter
  #  return calculatedBranches[(y,x)]
  elif(rows[y][x] == "^"):
    # calculate paths from this splitter
    output = 0
    output += laserPath(y+1, x-1)
    output += laserPath(y+1, x+1)
  #  calculatedBranches[(y,x)] = output
    return output
  else:
    # laser passed through empty space
    return laserPath(y+1, x)
    

for x in range(dataWidth):
  if(rows[0][x] == "S"):
    # laser start
    output = laserPath(1, x)
    break

print(output)
print(f"Time taken: {time.time() - start}")