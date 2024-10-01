def calculatePowerOfNumber(number,power):
    if power==1:
        return number * 1
    return number * calculatePowerOfNumber(number,power-1)

n,r,p=10,5,100
A=p*calculatePowerOfNumber(1+r/100,n)
print("Total amount is: ",A)