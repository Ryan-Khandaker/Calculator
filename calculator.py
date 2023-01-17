import math   #Allows access to mathematical operations which is not accessable by normal python operations

def inputs():
    operator = input ('What operation do you want to do? (add- addition, sub- subtraction, mult- multiplication, div- division, log- logarithm, exp- exponential, ln- natural logrithm, e- natural exponential, sqrt- square root): ') #Allows user to choose an operation
    while operator != 'add' and operator != 'sub' and operator != 'mult' and operator != 'div' and operator != 'log' and operator != 'exp' and operator != 'ln' and operator != 'e' and operator != 'sqrt':
        operator = input ('Invalid operator. Please insert a correct operation: ')
    if operator == 'add' or operator == 'sub' or operator == 'mult' or operator == 'div' or operator == 'log' or operator == 'exp':
        num1 = input ('Insert a value: ')
        adjust = num1.replace('-', '0', 1)
        adjust2 = adjust.replace('.', '0', 1)
        while adjust2.isnumeric() == False:
            num1 = input('Invalid input. Please insert a valid number: ')
            adjust = num1.replace('-', '0', 1)
            adjust2 = adjust.replace('.', '0', 1)
        value1 = float (num1)    
        num2 = input ('Insert a second value: ')   
        adjust3 = num2.replace('.','0', 1)
        adjust4 = adjust3.replace('-', '0', 1)
        while adjust4.isnumeric() == False:
            num2 = input ('Invalid entry. Please input a valid number: ')
            adjust3 = num2.replace('.','0', 1)
            adjust4 = adjust3.replace('-', '0', 1)
        value2 = float (num2)
    elif operator == 'ln' or operator == 'e' or operator == 'sqrt':
        num1 = input ('Insert a value: ')
        adjust = num1.replace('-', '0', 1)
        adjust2 = adjust.replace('.', '0', 1)
        while adjust2.isnumeric() == False:
            num1 = input ('Invalid entry. Please insert a valid number: ')
            adjust = num1.replace('-', '0', 1)
            adjust2 = adjust.replace('.', '0', 1)
        value1 = float(num1)
        value2 = 0
    print (operation(value1, value2, operator))

def operation(number1, number2, function):
    if function == 'add':
        result = number1 + number2          #Adds numbers
    elif function == 'sub':                
        result = number1 - number2              #Subtracts numbers
    elif function == 'mult':
        result = number1 * number2       #Multiplies numbers
    elif function == 'div':
        if number2 == 0:                #Does not allow denominator to be 0
            return "Number cannot be divided by 0"
        else:
            result = number1/number   #Divides numbers
    elif function =='log':
        if number1 <= 0 or number2 <=0:       
            return 'Inputs must be greater than 0'    #Does not allow invalid inputs
        else: 
            result = math.log(number1, number2)        # number1 is the number and number2 is the base
    elif function == 'exp':
        result = number1**number2                    #number1 is the base while number 2 is the exponent
    elif function == 'ln':
        if number1 <=0                                       #Check for invalid numbers
            return 'The function cannot run the calculation with this input. Please choose a number greater than 0'
        result = math.log(number1, math.e)           #Does natural logarithmic function
    elif function == 'e':
        result = math.e**number1                 #Does natural exponential function
    elif function == 'sqrt':
        if number1 <0:                              #Checks for invalid inputs
            return 'Input cannot be less than 0'
        else:            
            result = math.sqrt(number1)             #Does square root function
    return result

inputs()