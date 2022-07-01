class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # key value pairing
        numDict = {'1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '0':0}
        if num1 == "0" or num2 == "0":
            return '0'
        numList1 = [x for x in num1]
        numList2 = [x for x in num2]
        
        numList1.reverse()
        n1 = 0
        for n in range(len(numList1)):
            n1 += numDict[numList1[n]] * (10**n)
        
        numList2.reverse()
        n2 = 0
        for n in range(len(numList2)):
            n2 += numDict[numList2[n]] * (10**n)
        res = n1 * n2
        return(str(res))
        
