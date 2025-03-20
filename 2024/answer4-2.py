f = open("input4.txt","r")
data = []
for line in f:
  data.append(line.strip())

xCount = 0

for i in range(0,len(data)):
  row = data[i]
  for j in range(0,len(row)):
    if(row[j]== "A"):
      if(i >= 1 and j >= 1 and i <= len(data) - 2 and j <= len(row) - 2):
        print(i, j)
              # M  M
              #  A
              # S  S
        if(data[i-1][j-1] == "M" and data[i-1][j+1] == "M" and data[i+1][j+1] == "S" and data[i+1][j-1] == "S"):
          xCount += 1
              # M  S
              #  A
              # M  S
        if(data[i-1][j-1] == "M" and data[i-1][j+1] == "S" and data[i+1][j+1] == "S" and data[i+1][j-1] == "M"):
          xCount += 1
              # S  S
              #  A
              # M  M
        if(data[i-1][j-1] == "S" and data[i-1][j+1] == "S" and data[i+1][j+1] == "M" and data[i+1][j-1] == "M"):
          xCount += 1
              # S  M
              #  A
              # S  M
        if(data[i-1][j-1] == "S" and data[i-1][j+1] == "M" and data[i+1][j+1] == "M" and data[i+1][j-1] == "S"):
          xCount += 1
        
      
print(xCount)