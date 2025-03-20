f = open("input4.txt","r")
data = []
for line in f:
  data.append(line.strip())

xCount = 0

for i in range(0,len(data)):
  row = data[i]
  for j in range(0,len(row)):
    if(row[j]== "X"):
      up = True if i >= 3 else False
      down = True if i < len(data) - 3 else False
      left = True if j >= 3 else False
      right = True if j < len(row) - 3 else False
      
      print("i",i,"j",j,"up",up,"down",down,"left",left,"right",right)
      # check up
      if(up):
        if(data[i][j] == "X" and data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S"):
          xCount += 1
      # check up-right
      if(up and right):
        if(data[i][j] == "X" and data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S"):
          xCount += 1
      # check right
      if(right):
        if(data[i][j] == "X" and data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S"):
          xCount += 1
      # check down-right
      if(down and right):
        if(data[i][j] == "X" and data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S"):
          xCount += 1
      # check down
      if(down):
        if(data[i][j] == "X" and data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S"):
          xCount += 1
      # check down-left
      if(down and left):
        if(data[i][j] == "X" and data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S"):
          xCount += 1
      # check left
      if(left):
        if(data[i][j] == "X" and data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S"):
          xCount += 1
      # check up-left
      if(up and left):
        if(data[i][j] == "X" and data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S"):
          xCount += 1
      
print(xCount)