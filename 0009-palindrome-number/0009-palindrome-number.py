class Solution:
    import math
    def isPalindrome(self, x: int) -> bool:
        if x<0: 
            return False
        if x==0: 
            return True
        placeValue=int(math.log10(x))
        list_faceValue=[]
        temp_val=x
        for i in range(placeValue,0,-1):
            list_faceValue.append(int(temp_val/10**i))
            if i==1:
                list_faceValue.append(temp_val%10**i)
            else:
                temp_val=temp_val%10**i


        return list_faceValue == list_faceValue[::-1]







        