f = open("2025/input3.txt","r")

output = 0
for tempBank in f:
  bank = tempBank.strip()
  maxJoltage = 0
  bankLen = len(bank)

  chars = []
  charPositions = []

  largestCharPosition = 0
  startingPoint = 0
  for i in range(11, -1, -1): # controls how many digits we leave as a buffer at the end
    largestChar = -1
    for j in range(startingPoint, bankLen-i): # runs through current slice of data
      numBeingEvaluated = bank[j]
      if(int(bank[j])>int(largestChar)): # if digit in slice is biggest, record that
        largestChar = bank[j]
        largestCharPosition = j
    charPositions.append(largestCharPosition)
    chars.append(largestChar)
    startingPoint = largestCharPosition + 1
  print(chars)
  output += int("".join(chars))

  

print(output)