def findMaxWeight(allowedWeight, weights, profits, n ):
    if(n == 0 & allowedWeight ==0):
        return 0
    
    if(weights[n -1] > allowedWeight):
        return findMaxWeight(allowedWeight, weights, profits,n-1)
    else :
        return max(profits[n-1] + findMaxWeight(allowedWeight - weights[n-1],weights,profits,n-1),findMaxWeight(allowedWeight, weights,profits,n-1))
    

if __name__ == '__main__': 
    profit = [60, 100, 120] 
    weight = [10, 20, 30] 
    W = 50
    n = len(profit) 
    print(f"Results: ",findMaxWeight(W, weight, profit, n) )