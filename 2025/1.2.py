f = open("input1.txt","r")

# Got annoyed by all the edge cases and went with possibly the least
# optimized method. Yes, I know it's awful

zeroTally = 0
val = 50
message = ""
for line in f:
  direction = line.strip()[0:1]
  distance = int(line.strip()[1:])
  
  if(direction == "R"):
    for i in range(distance):
      val += 1
      if(val == 0):
        zeroTally += 1
      elif(val == 100):
        zeroTally += 1
        val = 0
  
  elif(direction == "L"):
    for i in range(distance):
      val -= 1
      if(val == 0):
        zeroTally += 1
      elif(val == -1):
        val = 99
  
  
print(zeroTally)
