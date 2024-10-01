class samples:
    def __init__(self,size) -> None:
        self.output = [0] * size
        self.top1  = -1
        self.top2 = size 
        
    def create_two_stack(self, input1, input2):
        try:
            #output = list(range(len(input1) + len(input2)))
            self.output= [0] * (len(input1) + len(input2))
            for i in range(0,len(input1)):
                self.output[i] = input1[i]
            j = len(input1)
            for i in range(len(input2)):
                self.output[j] =  input2[i]
                j+=1
            print(f'Result array: ', self.output)
            return self.output
        except Exception as exc:
            print("exception: ", str(exc))
    
    def push_to_stack1(self,item):
       #midpoint  = len(self.output)//2
       self.top1=self.top1+1
       self.output[self.top1] = item 
       print(f"result array after push to stack 1: ", self.output)       
    
    def push_to_stack2(self, item):
        #midpoint = len(self.output)//2
        self.top2 = self.top2 - 1
        self.output[self.top2] = item
        print(f"result array after push to stack 2: ", self.output)

    def pop_from_stack1(self):
        #midpoint  = len(self.output)//2 - 1
        print(f"item popped from stack 1: ",self.output[self.top1])
        self.output[self.top1]=0
        self.top1-=1
        print(f"result array after pop from stack 1: ", self.output)
    
    def pop_from_stack2(self):
        #midpoint1  = self.midpoint + 1
        print(f"item popped from stack 2: ",self.output[self.top2])
        self.output[self.top1]=0
        self.top2+=1
        print(f"result array after pop from stack 2: ", self.output)

class intFunctions:
    def __init__(self) -> None:
        pass
    def sortArray(self, input):
        print(f"sorted array: ", sorted(input))

    def findIntersection(self,input1, input2):
        output=[]
        for i in input1:
            if i in input2:
                output.append(i)
        print(f"intersection: ",output)

    def findNextGreater(self,input):
        for i in range(0,len(input),1):
            next = -1
            for j in range(i+1,len(input),1):
                if(input[i]<input[j]):
                    next=input[j]
                    break

            print(str(input[i])+"-->"+str(next))
    
if __name__ == '__main__': 
    c= samples(10)
    #input1 = [1,2,3,4,5]
    #input2 = [6,7,8,9,10]
    #c.create_two_stack(input1, input2)
    '''
    c.push_to_stack1(11)    
    c.push_to_stack1(12)
    c.push_to_stack1(13)
    c.push_to_stack2(16)
    c.push_to_stack2(15)
    c.push_to_stack2(14)
    c.pop_from_stack1()
    c.pop_from_stack1()
    c.pop_from_stack1()
    c.pop_from_stack2()
    c.pop_from_stack2()
    c.pop_from_stack2()
    '''
    c2 = intFunctions()
    #c2.sortArray([0,2,1,2,1,0])
    #c2.findIntersection([7,2,3,5,6],[6,3,2])
    c2.findNextGreater([11,13,21,3])

