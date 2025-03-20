import re
f = open("input3.txt","r")
input = f.read()

total = 0
validInstructions = re.findall("mul\(\d{1,3},\d{1,3}\)",input)
for instruction in validInstructions:
  nums = re.findall("\d{1,3}",instruction)
  total += int(nums[0]) * int(nums[1])
print(total)
