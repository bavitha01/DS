class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        for row in range(1,numRows+1):
            ans.append(self.generateRow(row))
        return ans
    def generateRow(self,row):
        ans=1
        ansRow=[1]
        for col in range(1,row):
            ans=ans*(row-col)
            ans=ans//col
            ansRow.append(ans)
        return ansRow