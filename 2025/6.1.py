import re
f = open("2025/input6.txt","r")

lines = []
for line in f:
  lines.append(
    re.split(r'\s+',line.strip())
  )

dataWidth = len(lines[0])
dataHeight = len(lines) - 1
output = 0

for x in range(dataWidth):
  operator = lines[dataHeight][x]
  problemTally = int(lines[0][x])
  for y in range(1, dataHeight):
    if(operator == "+"):
      problemTally += int(lines[y][x])
    elif(operator == "*"):
      problemTally *= int(lines[y][x])
  output += problemTally


print(output)
