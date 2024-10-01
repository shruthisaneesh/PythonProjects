class MaximumSumSubset:
    def __init__(self, sum) -> None:
        self.sum = 0
        self.subsetArray = []
    def findMaximumSumSubset(self,input):
        self.sum=0
        itr = 0
        maxSum = 0
        for i in range(0,len(input)-1):
            subsetArray=[]
            #maxSum = 0
            maxSum = maxSum + input[i]
            if(maxSum > self.sum):
                self.sum = maxSum

            elif (maxSum < 0):
                maxSum=0

            '''
            j=len(input)
            while(j>0):
                itr+=1
                subsetArray=input[i:j]
                subsetSum=sum(subsetArray)
                if (subsetSum > self.sum) :
                    self.sum= subsetSum
                    self.subsetArray= subsetArray
                j-=1
            '''

        return self.sum

if __name__ == '__main__':
    c= MaximumSumSubset(0)
    print(f"Result subset: ",c.findMaximumSumSubset([-2,-3,4,-1,-2,1,5,-3]) )