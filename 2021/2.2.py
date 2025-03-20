f = open("folder/input2.txt","r")
file = f.readlines()
length = len(file)
x = 0
y = 0
aim = 0
for i in range(0,len(file)):
    instruction = file[i].strip()
    valueFlag = False
    movement = ""
    value = ""
    for j in range(0, len(instruction)):
        if instruction[j] == " ":
            valueFlag = True
        elif valueFlag == False:
            movement = movement + instruction[j]
        else:
            value = value + instruction[j]
    value = int(value)
    if movement == "forward":
        x = x + value
        y = y + (value*aim)
    elif movement == "up":
        aim = aim - value
    else:
        aim = aim + value


print("X value is:", x)
print("Y value is:", y)
print("X * Y is equal to:", x*y)

f.close()