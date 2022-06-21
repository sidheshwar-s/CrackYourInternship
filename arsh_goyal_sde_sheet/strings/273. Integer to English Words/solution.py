class Solution:
    def numberToWords(self, num):
        def helper(num):
            if num < 10:
                return dic1[num]
            elif 10 <= num < 20:
                return dic3[num]
            elif num < 100:
                res = []
                q, num = divmod(num, 10)
                res.append(dic2[q*10])
                if num > 0:
                    res.append(" "+dic1[num])
                return "".join(res)
            elif num < 1000:
                q, num = divmod(num, 100)
                if num == 0:
                    return dic1[q]+" "+"Hundred"
                else:
                    return dic1[q]+" "+"Hundred"+" "+helper(num)
            elif num < 1000000:
                q, num = divmod(num, 1000)
                if num == 0:
                    return helper(q)+" "+"Thousand"
                else:
                    return helper(q)+" "+"Thousand"+" "+helper(num)
            elif num < 1000000000:
                q, num = divmod(num, 1000000)
                if num == 0:
                    return helper(q)+" "+"Million"
                else:
                    return helper(q)+" "+"Million"+" "+helper(num)
            else:
                q, num = divmod(num, 1000000000)
                if num == 0:
                    return helper(q)+" "+"Billion"
                else:
                    return helper(q)+" "+"Billion"+" "+helper(num)  
                
        if num == 0:
            return "Zero"
        
        dic1 = {9:"Nine", 8:"Eight", 7:"Seven", 6:"Six", 
                5:"Five", 4:"Four", 3:"Three", 2:"Two", 1:"One"}
        dic2 = {90:"Ninety", 80:"Eighty", 70:"Seventy", 60:"Sixty", 
                50:"Fifty", 40:"Forty", 30:"Thirty", 20:"Twenty"} 
        dic3 = {19:"Nineteen", 18:"Eighteen", 17:"Seventeen", 
                16:"Sixteen", 15:"Fifteen", 14:"Fourteen", 13:"Thirteen", 
                12:"Twelve", 11:"Eleven", 10:"Ten"}
        
        return helper(num)