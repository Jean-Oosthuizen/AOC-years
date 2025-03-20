with open("folder/input3.txt", 'r') as f:
    lines = f.readlines()
    diagnostics = [entry.strip() for entry in lines]
gamma, epsilon = '', ''
for i in range(len(diagnostics[0])):
    all_entries_at_pos = [entry[i] for entry in diagnostics]
    if all_entries_at_pos.count('0') > len(diagnostics)/2:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

#print(int(gamma, base=2)*int(epsilon, base=2)) # the power consumption = task solution
from copy import copy

oxygen_diagnostics = copy(diagnostics)
for i in range(len(diagnostics[0])):
    if len(oxygen_diagnostics) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in oxygen_diagnostics]
    common_bit = '1' if all_entries_at_pos.count('1') >= len(oxygen_diagnostics)/2 \
                 else '0'
    oxygen_diagnostics = [entry for entry in oxygen_diagnostics 
                                    if entry[i]==common_bit]
oxygen_rating = int(oxygen_diagnostics[0], base=2)
print('oxygen', oxygen_diagnostics[0], oxygen_rating)
co2_diagnostics = copy(diagnostics)
for i in range(len(diagnostics[0])):
    if len(co2_diagnostics) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in co2_diagnostics]
    least_common_bit = '0' if all_entries_at_pos.count('1') >= len(co2_diagnostics)/2 \
                       else '1'
    co2_diagnostics = [entry for entry in co2_diagnostics
                                 if entry[i]==least_common_bit]
co2_rating = int(co2_diagnostics[0], base=2)
print('co2', co2_diagnostics[0], co2_rating)
print('life support rating', oxygen_rating*co2_rating)