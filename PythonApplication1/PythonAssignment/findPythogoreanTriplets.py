import math

def findPythogoreanTriplets(n):
    triplets=[]
    for i in range(1,n+1):
        for j in range(i,n+1):
            c_squared= i*i +j*j
            c = int(c_squared ** 0.5)
            if c_squared <= n and c_squared == c*c:
                triplets.append((i,j,c))

    return triplets

print("result: ",findPythogoreanTriplets(169))
