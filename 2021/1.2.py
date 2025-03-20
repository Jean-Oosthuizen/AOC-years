f = open("folder/input1.txt","r")
file = f.readlines()
length = len(file)
increaseCount = 0

num1 = int(file[0].strip())
num2 = int(file[1].strip())
num3 = int(file[2].strip())
numSum1 = num1+num2+num3
for i in range(1,length-2):
    num1 = int(file[i].strip())
    num2 = int(file[i+1].strip())
    num3 = int(file[i+2].strip())
    numSum2 = num1+num2+num3

    if numSum2 > numSum1:
        increaseCount += 1
    numSum1 = numSum2
print("The total increaseCount is:", increaseCount)
f.close()