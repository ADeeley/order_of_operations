# takes a string from the user and splits this into a list

# to do:
# 1. add iterators to recursive functions
equation = input("Please input the equation you would like to step through. \n")
eq_list = equation.split(" ")

def div_run(eq_list):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "/":
            n = n
            print("Step: ", eq_list[n-1], " / ", eq_list[n+1])
            temp = float(eq_list[n-1]) / float(eq_list[n+1]) # holds the equated value   
            eq_list[n] = temp # inserts temp into the list and removes the used numbers
            del eq_list[n+1]
            del eq_list[n-1]
            print(eq_list)
            break
    
    # checks if the operator is still in eq_list and calls the run again. Moves onto the 
    # next operator in bidmas if not.
    if "/" in eq_list and len(eq_list) > 1:
        div_run(eq_list)
    elif "*" in eq_list and len(eq_list) > 1:
        multi_run(eq_list)
    elif "+" in eq_list and len(eq_list) > 1:
        plus_run(eq_list)
    elif "-" in eq_list and len(eq_list) > 1:
        minus_run(eq_list)

def multi_run(eq_list):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "*":
            n = n
            print("Step: ", eq_list[n-1], " * ", eq_list[n+1])
            temp = int(eq_list[n-1]) * int(eq_list[n+1])
            eq_list[n] = temp
            del eq_list[n+1]
            del eq_list[n-1]
            print(eq_list)
            break
    
    if "*" in eq_list and len(eq_list) > 1:
        multi_run(eq_list)
    elif "+" in eq_list and len(eq_list) > 1:
        plus_run(eq_list)
    elif "-" in eq_list and len(eq_list) > 1:
        minus_run(eq_list)
        
def plus_run(eq_list):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "+":
            n = n
            print("Step: ", eq_list[n-1], " + ", eq_list[n+1])
            temp = int(eq_list[n-1]) + int(eq_list[n+1])
            eq_list[n] = temp
            del eq_list[n+1]
            del eq_list[n-1]
            print(eq_list)
            break
    
    if "+" in eq_list and len(eq_list) > 1:
        plus_run(eq_list)
    elif "-" in eq_list and len(eq_list) > 1:
        minus_run(eq_list)

def minus_run(eq_list):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "-":
            n = n
            print("Step: ", eq_list[n-1], " - ", eq_list[n+1])  
            temp = int(eq_list[n-1]) - int(eq_list[n+1])
            eq_list[n] = temp
            del eq_list[n+1]
            del eq_list[n-1]
            print(eq_list)
            break
    
    if len(eq_list) > 1:
        minus_run(eq_list)        
        
div_run(eq_list)   # calls the highest function from bidmas given - only 'dmas ATM
   