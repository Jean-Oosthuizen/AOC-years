f = open("2025/input3.txt","r")

output = 0
for tempBank in f:
  bank = tempBank.strip()
  maxJoltage = 0
  bankLen = len(bank)                                                   


  for i, char1 in enumerate(bank.strip()):
    for j, char2 in enumerate(bank[i+1:bankLen]):
      comboVal = int(char1+char2)
      if(comboVal > maxJoltage):
        maxJoltage = comboVal
  output += maxJoltage

  

print(output)