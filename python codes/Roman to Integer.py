s = "MCMXCIV"  
dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
total = 0


for i in range(len(s)):
    current_value = dic[s[i]]
    
    
    if i + 1 < len(s) and current_value < dic[s[i + 1]]:
        total -= current_value  
    else:
        total += current_value  

print(total)