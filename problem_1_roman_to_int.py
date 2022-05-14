class Solution:
    def romanToInt(self, s: str) -> int:
        allowed_char = ['I','V','X','L','C','D','M']
        allowed_char_values = [1,5,10,50,100,500,1000]
        
        sum = 0
        i = 0
        if 1 <= len(s) and len(s)<= 15:
            while i < len(s):
                #print('i = ',i, 'Working Roman digit = ',s[i],'total len = ',len(s))
                if s[i] not in allowed_char:
                    #print('Invalid input')
                    return -1
                
                if i < (len(s)-1) and allowed_char.index(s[i]) < allowed_char.index(s[i+1]):
                    #print('Multiple digit number exists.')
                    temp_sum = allowed_char_values[allowed_char.index(s[i+1])] - allowed_char_values[allowed_char.index(s[i])]
                    sum += temp_sum
                    #print('multiple digit section Sum = ',sum)
                    #print('current index = ',i)
                    i += 1
                    #print('current index increased= ',i)

                else:
                    found_index = allowed_char.index(s[i])
                    #print(s[i],' ',found_index)
                    sum += allowed_char_values[found_index]
                    #print('Sum = ',sum)
                
                i +=1
                    
            #print(sum)
            return sum
        else:
            return -1
            
            
        
        
a = Solution()
print(a.romanToInt('MCMXCIVMCMXCIVMCMXCIV'))

