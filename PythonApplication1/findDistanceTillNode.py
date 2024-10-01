class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left=self.right=None
    
def newNode(data):
    node= Node(data)
    return node

def Kdistance(root,k):
    result =[]
    stack = []
    stack.append((root,0))

    while stack:
        curr,level = stack.pop()

        if curr is None:
            continue

        if level == k:
            result.append(curr.data)

        stack.append((curr.right,level+1))

        stack.append((curr.left,level+1))

    return result

root = newNode(1)
root.left = newNode(10)
root.right = newNode(4)
root.left.left = newNode(8)
root.left.right = newNode(10)

k=2
result=Kdistance(root,k)
print(f"Result: ",result)