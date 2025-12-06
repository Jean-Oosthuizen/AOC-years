f = open("2025/input6.txt","r")

lines = []
for line in f:
  lines.append(line.replace("\n",""))

dataWidth = len(lines[0])
dataHeight = len(lines) - 1

problemTally = 0
output = 0
firstNumberInProblem = True

for x in range(dataWidth):

  # a new problem has started
  if(lines[dataHeight][x] != " "):
    output += problemTally
    problemTally = 0
    firstNumberInProblem = True
    operator = lines[dataHeight][x]
  
  # extract number from column
  fullLine = ""
  num = ""
  for y in range(0, dataHeight):
    thisChar = lines[y][x]
    fullLine += thisChar
    if(thisChar != " "):
      num += lines[y][x]
  
  # perform operation
  if(num != ""):
    if(operator == "+"):
      problemTally += int(num)
    elif(operator == "*"):
      if(firstNumberInProblem):
        firstNumberInProblem = False
        problemTally = int(num)
      else:
        problemTally *= int(num)

output += problemTally
  
print(output)
