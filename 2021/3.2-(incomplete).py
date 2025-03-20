#Finds the most common bits in each bit position
def mostCommonBits():
    binlist = []
    #repeats for every column
    for j in range(0,lineLength):
        binlist.append(0)
        #counts the number of bits in that column across every row
        for i in range(0,fileLength):
            line = file[i].strip()
            binlist[j] = binlist[j] + int(line[j])

        
        #checks if the number of 1's are the majority in that column
        if binlist[j] > half:
            binlist[j] = 1
        elif binlist[j] == half:
            binlist[j] = 1
        else:
            binlist[j] = 0     
    print("Binlist",binlist)
    return binlist

#searches through the document for the specific reading
def oxygenRating(f, type):
    valid = f
    #repeats the process for every column, with a smaller valid list every time
    for j in range(0,lineLength):
        #finds the current bit depending on what data points you want to get. So normal values for Oxygen, inverted values for CO2 scrubber
        if type == "Oxygen":
            currentBit = binlist[j]
        else:
            if binlist[j] == 1:
                currentBit = "0"
            else:
                currentBit = "1"
        validLength = len(valid)
        poppers = []
        #if the bit found at line[j] is not valid, then that line is queued to be popped
        for i in range(0,validLength):
            line = valid[i].strip()
            if line[j] != str(currentBit) and len(valid) != 1:
                poppers.append(i)
        #pops everything that was queued
        for j in range(len(poppers)-1,-1,-1):
            valid.pop(poppers[j])
        print(valid)
        input()
    return valid[0].strip()
  

        
#opens file, generates metadata about the file
f = open("folder/input3.txt","r")
file = f.readlines()
fileLength = len(file)
lineLength = len(file[0].strip())
half = int(fileLength/2)

#finds the most common bits in the file for every column
binlist = mostCommonBits()

#finds the value for the Oxygen reading
oxygen = oxygenRating(file, "Oxygen")

#refreshes the stored file, since the function changes the value here for a reason I don't know
f.close()
f = open("folder/input3.txt","r")
file = f.readlines()
#finds the CO2 reading
CO2 = oxygenRating(file, "CO2")

oxygenDec = int(str(oxygen.strip()),2)
CO2Dec = int(str(CO2.strip()),2)
print("Oxygen:", oxygen, oxygenDec)
print("CO2:", CO2, CO2Dec)
print("Multiplied:", oxygenDec*CO2Dec)
