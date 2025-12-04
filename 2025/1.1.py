f = open("input1.txt","r")

zeroTally = 0
val = 50
for line in f:
  direction = line.strip()[0:1]
  distance = int(line.strip()[1:])
  if(direction == "R"):
    print(val, "+", distance)
    val += distance
    if(val >= 100):
      val -= 100
    print("=",val)

  elif(direction == "L"):
    print(val, "-", distance)
    val -= distance
    if(val < 0):
      val += 100
    print("=",val)

  else:
    raise Exception("Invalid direction")
  
  if(val == 0):
    zeroTally += 1

print(zeroTally)
