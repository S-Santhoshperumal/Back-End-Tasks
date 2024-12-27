def addition(value1,value2):
    return value1+value2
def subtraction(value1,value2):
    return value1-value2
def multiplication(value1,value2):
    return value1*value2
def divide(value1,value2):
    return value1/value2
def floordivide(value1,value2):
    return value1//value2
def power(value1,value2):
    return value1**value2

def main():
    symbol=input('select your symbol : ')
    value1=int(input('enter your first number : '))
    value2=int(input('enter your second number : '))
    
    if(symbol=='+'): 
        print(addition(value1,value2))
    elif(symbol=='-'): 
        print(subtraction(value1,value2))
    elif(symbol=='*'): 
        print(multiplication(value1,value2))
    elif(symbol=='/'): 
        print(divide(value1,value2))
    elif(symbol=='//'): 
        print(floordivide(value1,value2))
    elif(symbol=='**'): 
        print(power(value1,value2))
    else: print('your had entered a wrong one')
    

if __name__=='__main__':
    main()