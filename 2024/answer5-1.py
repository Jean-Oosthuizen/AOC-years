import math
f = open("input5.txt","r")

rulesDone = False
rules = []
updates = []
for line in f:
  if(rulesDone == False):
    if(line == "\n"):
      rulesDone = True
    else:
      rules.append(line.strip())
  else:
    updates.append(line.strip())
    
middleNums = 0
for update in updates:
  updateValid = True
  for rule in rules:
    num1 = rule.split("|")[0]
    num2 = rule.split("|")[1]
    
    num1index = -1
    num2index = -1
    
    pages = update.split(",")  
    for i in range(0,len(pages)):
      page = pages[i]
      if(page == num1):
        num1index = i
      elif(page == num2):
        num2index = i
    
    if(num1index != -1 and num2index != -1):
      if(num1index > num2index):
        updateValid = False
        break
  if(updateValid):
    print(len(pages),math.floor(len(pages)/2),pages[math.floor(len(pages)/2)],pages)
    middleNums += int(pages[math.floor(len(pages)/2)])
    
print(middleNums)