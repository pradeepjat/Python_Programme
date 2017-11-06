def increment(number):
    '''
    Objective: To find a increment of a number
    Input Parrameter: 
             number->incrementing number 
    Return : incremented value of no.
    '''
    #Approach : number++
    
    number=number+1
    return number
    
def decrement(number):
    '''
    Objective: To find a decrement of a number
    Input Parrameter: 
             number->decrementing number 
    Return : decrement value of no.
    '''
    #Approach : number--
    
    number=number-1
    return number
    
def recursivly_sum(number1,number2):
    '''
    Objective: To find a addition of two number using recursion
    Input Parrameter: 
             number1->first number enter by user 
             number2->second number enter by user 
    return : addition of two no.             
    '''
    #Approach : recursivly
    
    if number2==0:
        return number1
    else:
        number1=increment(number1)
        number2=decrement(number2)
        return recursivly_sum(number1,number2)

def main():
    '''
    Objective: To find a sum of a no. recursivly and using a increment and decrement function
    Input Parrameter:
             number1->first number enter by user 
             number2->second number enter by user  
    Output Parrameter: 
             addition -> contain final addition
    '''
    # Approach : By calling the function  recursivly_sum()
    
    number1 = int(input("Enter First no.for addition: "))
    number2 = int(input("Enter second no. for addition: "))
    addition = recursivly_sum(number1,number2)
    print(number1,'+',number2,"=",addition)
    
if __name__ =="__main__":
    main()
