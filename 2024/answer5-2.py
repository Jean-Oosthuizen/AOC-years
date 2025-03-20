import math
f = open("input5 sample2.txt","r")

#extract data from file
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
    
# find the bad updates
middleNums = 0
badUpdates = []
for update in updates:
  pages = update.split(",")  
  for rule in rules:
    num1 = rule.split("|")[0]
    num2 = rule.split("|")[1]
    
    num1index = -1
    num2index = -1
    for i in range(0,len(pages)):
      page = pages[i]
      if(page == num1):
        num1index = i
      elif(page == num2):
        num2index = i
    
    if(num1index != -1 and num2index != -1):
      if(num1index > num2index):
        badUpdates.append(update)
        break
      
# fix bad updates
fixedUpdates = []
for update in badUpdates:
  pages = list(map(int,update.split(","))) 
  for rule in rules:
    sorted = False
    num1 = int(rule.split("|")[0])
    num2 = int(rule.split("|")[1])
    num1inHere = num1 in pages
    num2inHere = num2 in pages
    if(num1inHere and num2inHere and not sorted):
       
      # if num1 is later in the list than num2
      if(pages.index(num1) > pages.index(num2)):
        caughtnum2 = False
        for i in range(0,len(pages)):
          #loop through until 
          if(pages[i] == num2):
            caughtnum2 = True
          if(caughtnum2):
            temp1 = pages[i+1]
            pages[i+1] = pages[i]
            pages[i] = temp1
            if(pages[i] == num1):
              break
            
  fixedUpdates.append(",".join(map(str, pages)))

# count the number of updates that have been fixed, and sum middle numbers
fixedCounter = 0
middleNums = 0
for update in fixedUpdates:
  pages = update.split(",")  
  for rule in rules:
    num1 = rule.split("|")[0]
    num2 = rule.split("|")[1]
    
    num1index = -1
    num2index = -1
    for i in range(0,len(pages)):
      page = pages[i]
      if(page == num1):
        num1index = i
      elif(page == num2):
        num2index = i
    
    if(num1index != -1 and num2index != -1):
      if(num1index < num2index):
        fixedCounter += 1
        middleNums += int(pages[math.floor(len(pages)/2)])
        break

print(fixedCounter, "/", len(badUpdates))
print(middleNums)