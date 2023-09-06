'''
Counting Bits, LeetCode
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        List=[]
        for i in range(n+1):
            k=0
            a=list(bin(i))
            for num in a:
                if num == '1':
                    k+=1
            List.append(k)
        return(List)
