f = open("folder/input3.txt","r")
file = f.readlines()
fileLength = len(file)
lineLength = len(file[0].strip())
half = fileLength/2
binlist = []
gamma = ""
epsilon = ""

for j in range(0,lineLength):
    binlist.append(0)
    for i in range(0,fileLength-1):
        line = file[i].strip()
        binlist[j] = binlist[j] + int(line[j])

for k in range(0,lineLength):
    if binlist[k] > half:
        gamma =  gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma =  gamma + "0"
        epsilon = epsilon + "1"
print("Gamma: ",int(gamma,2)," Epsilon:", int(epsilon,2))
print("Multiplied together:",int(gamma,2)*int(epsilon,2))