f = open("folder/input1.txt","r")
file = f.readlines()
length = len(file)
num1 = int(file[0].strip())
increaseCount = 0
for i in range(1,length):
    num2 = int(file[i].strip())
    if num2 > num1:
        increaseCount += 1
    num1 = num2
print("The total increaseCount is:", increaseCount)
f.close()