def string_functions_test(message):
    print(message.split())
    #print("message after replacing t with d is "+message.replace('t','d'))
    #print(type(message))

def int_functions_test(input):
    for i in range(input):
        print(i,end='\n')

def find_character(input, character):
    count=0
    for i in range(len(input)):
        if(input[i]==character):
            count=count+1
    print("Number of occurence: "+ count)

def reverse_string(input):
    stack = create_stack()
    reversedString=""
    try:
        for i in input:
            push(stack, i)

        for i in range(len(stack)):
            reversedString+=pop(stack)
    except (ValueError, TypeError) as e:
        print("Exception: ", e)

    print("reversed string: ",reversedString)

def test_slicing(input):
    print("sliced string: ", input[slice(1,6,7)])

def create_stack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack) == 0:
        return 
    return stack.pop()

def find_unique_character(input):
   
    char_set ={}

    for a in input:
        if a not in char_set.keys():
            char_set[a] = 1
        else :
            char_set[a]+=1

    for a in input:
        if (char_set[a]== 1):
            return a
    return None

def find_missing_number_in_array(array):
    array.sort()
    sum1 = 0
    n = array[-1]
    formula_sum = n*(n+1)//2
    sum1 = sum(array)

    print("missing number in array is: ", (formula_sum - sum1))

def print_fib_series(n):
    a,b = 0,1
    for i in range(1,n):
        print (a)
        a , b = b, a+b

def test_generator(array):
    result = [x+2 for x in array]
    print ("Result: ",result)


#string_functions_test("My name is shruthi saneesh")
#int_functions_test(20)
#find_character("My name is shruthi saneesh",'s')
#reverse_string("Ilovedogs")
#test_slicing("asddddhjhjh")
#print (find_unique_character("aaajjhjaahhjjiaaa"))
#find_missing_number_in_array([4,2,6,7,3,1,8])
#print_fib_series(10)
test_generator([2,4,6,8,10])

