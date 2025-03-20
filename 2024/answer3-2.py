import re
f = open("input3.txt","r")
input = f.read()

total = 0
validInstructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",input)
enabled = True
for instruction in validInstructions:
  if(instruction == "do()"):
    enabled = True
    continue 
  elif(instruction == "don't()"):
    enabled = False
    continue 
  
  if(enabled):
    print(instruction)
    nums = re.findall(r"\d{1,3}",instruction)
    total += int(nums[0]) * int(nums[1])
print(validInstructions)
print(total)
