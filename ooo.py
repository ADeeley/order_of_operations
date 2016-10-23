# ------------------------------------
# BIDMAS Walker, v 0.1, 
# coded by Adam Deeley 
# ------------------------------------

# to do:
# 1. add iterators to recursive functions
# 2. clean up logic
# 3 round to 2 dp

# takes a string from the user and splits this into a list
equation = input("Please input the equation you would like to step through. \n")

eq_list = equation.split(" ")

# checks for duplicate spaces
xs_spaces = []

def list_parse(eq_list):
    xNew = []
    for n in range(0, len(eq_list)):
        if xNew == []:
            xNew.append("")
        elif eq_list[n] == " ":
            continue
        elif eq_list[n] in ("1","2","3","4","5","6","7","8","9","0"):
            xNew[-1] = xNew[-1] + eq_list[n]
        else:
            xNew.append(eq_list[n])
            xNew.append("")    
            return xNew
           
    for n in xNew:
        try:
            int(xNew[n])
        except ValueError:
            continue
    
eq_list = list_parse(eq_list)    
step = 0

def initial_test(eq_list, step):
    if "**" in eq_list and len(eq_list) > 1:
        int_run(eq_list, step)
    elif "/" in eq_list and len(eq_list) > 1:
        div_run(eq_list, step)
    elif "*" in eq_list and len(eq_list) > 1:
        multi_run(eq_list, step)
    elif "+" in eq_list and len(eq_list) > 1:
        plus_run(eq_list, step)
    elif "-" in eq_list and len(eq_list) > 1:
        minus_run(eq_list, step)
    else:
        print("Done")

def int_run(eq_list, step):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    step += 1
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "**":
            n = n
            print("\nStep %s:" % step)
            print(eq_list[n-1], " ** ", eq_list[n+1])
            temp = float(eq_list[n-1]) ** float(eq_list[n+1]) # holds the equated value   
            eq_list[n] = temp # inserts temp into the list and removes the used numbers
            del eq_list[n+1]
            del eq_list[n-1]
            print("Updated equation: ", eq_list)
            break
    
    # checks if the operator is still in eq_list and calls the run again. Moves onto the 
    # next operator in bidmas if not.
    if "**" in eq_list and len(eq_list) > 1:
        int_run(eq_list, step)
    elif "/" in eq_list and len(eq_list) > 1:
        div_run(eq_list, step)
    elif "*" in eq_list and len(eq_list) > 1:
        multi_run(eq_list, step)
    elif "+" in eq_list and len(eq_list) > 1:
        plus_run(eq_list, step)
    elif "-" in eq_list and len(eq_list) > 1:
        minus_run(eq_list, step)
    else:
        print("Done")

def div_run(eq_list, step):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    step += 1
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "/":
            n = n
            print("\nStep %s:" % step)
            print(eq_list[n-1], " / ", eq_list[n+1])
            temp = float(eq_list[n-1]) / float(eq_list[n+1]) # holds the equated value   
            eq_list[n] = temp 
            del eq_list[n+1]
            del eq_list[n-1]
            print("Updated equation: ", eq_list)
            break
    
    if "/" in eq_list and len(eq_list) > 1:
        div_run(eq_list, step)
    elif "*" in eq_list and len(eq_list) > 1:
        multi_run(eq_list, step)
    elif "+" in eq_list and len(eq_list) > 1:
        plus_run(eq_list, step)
    elif "-" in eq_list and len(eq_list) > 1:
        minus_run(eq_list, step)
    else:
        print("Done")
def multi_run(eq_list, step):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    step += 1
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "*":
            n = n
            print("\nStep %s:" % step)
            print(eq_list[n-1], " * ", eq_list[n+1])
            temp = int(eq_list[n-1]) * int(eq_list[n+1])
            eq_list[n] = temp
            del eq_list[n+1]
            del eq_list[n-1]
            print("Updated equation: ", eq_list)
            break
    
    if "*" in eq_list and len(eq_list) > 1:
        multi_run(eq_list, step)
    elif "+" in eq_list and len(eq_list) > 1:
        plus_run(eq_list, step)
    elif "-" in eq_list and len(eq_list) > 1:
        minus_run(eq_list, step)
    else:
        print("Done")
        
def plus_run(eq_list, step):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    step += 1
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "+":
            n = n
            print("\nStep %s:" % step)
            print(eq_list[n-1], " + ", eq_list[n+1])
            temp = int(eq_list[n-1]) + int(eq_list[n+1])
            eq_list[n] = temp
            del eq_list[n+1]
            del eq_list[n-1]
            print("Updated equation: ", eq_list)
            break
    
    if "+" in eq_list and len(eq_list) > 1:
        plus_run(eq_list, step)
    elif "-" in eq_list and len(eq_list) > 1:
        minus_run(eq_list, step)
    else:
        print("Done")

def minus_run(eq_list, step):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    step += 1
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "-":
            n = n
            print("\nStep %s:" % step)
            print(eq_list[n-1], " - ", eq_list[n+1])  
            temp = int(eq_list[n-1]) - int(eq_list[n+1])
            eq_list[n] = temp
            del eq_list[n+1]
            del eq_list[n-1]
            print("Updated equation: ", eq_list)
            break
    
    if len(eq_list) > 1:
        minus_run(eq_list, step)   
    else:
        print("-----Done-----")        
        
initial_test(eq_list, step)   # calls the highest function from bidmas given - only 'dmas ATM
   