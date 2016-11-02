""" ------------------------------------
BIDMAS Walker, v 0.1, 
coded by Adam Deeley 

to do:
1. add iterators to recursive functions
3 round to 2 dp
4 call float once on the list instead of each function call
------------------------------------"""
# variables:
decimal_places = 3 

# takes a string from the user and splits this into a list
equation = input("Please input the equation you would like to step through. \n")

eq_list = equation.split(" ")

# checks for duplicate spaces
xs_spaces = []

step = 0

def find_operands(eq_list, step):
    if "**" in eq_list or "/" in eq_list or "*" in eq_list or "+" in eq_list or "-" in eq_list and len(eq_list) > 1:
        run(eq_list, step)
    else:
        print("Done")

def run(eq_list, step):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    step += 1
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] in ["**", "/", "*", "+", "-"]:
            if eq_list[n] == "**":
                n = n
                print("\nStep %s:" % step)
                print(eq_list[n-1], " ** ", eq_list[n+1])
                temp = float(eq_list[n-1]) ** float(eq_list[n+1])
            elif eq_list[n] == "/":
                n = n
                print("\nStep %s:" % step)
                print(eq_list[n-1], " / ", eq_list[n+1])
                temp = round(float(eq_list[n-1]) / float(eq_list[n+1]))
            elif eq_list[n] == "*":
                n = n
                print("\nStep %s:" % step)
                print(eq_list[n-1], " * ", eq_list[n+1])
                temp = float(eq_list[n-1]) * float(eq_list[n+1])         
            elif eq_list[n] == "+":
                n = n
                print("\nStep %s:" % step)
                print(eq_list[n-1], " + ", eq_list[n+1])
                temp = float(eq_list[n-1]) + float(eq_list[n+1])
            elif eq_list[n] == "-":
                n = n
                print("\nStep %s:" % step)
                print(eq_list[n-1], " - ", eq_list[n+1])
                temp = float(eq_list[n-1]) - float(eq_list[n+1])                 
            eq_list[n] = temp # inserts temp into the list and removes the used numbers
            del eq_list[n+1]
            del eq_list[n-1]
            
            string_eq = ""
            for n in eq_list: # makes a string representation of eq_list
                string_eq += str(n) + " "
                
            print("Updated equation: ", string_eq)
            break
    
    # checks if the operator is still in eq_list and calls the run again. Moves onto the 
    # next operator in bidmas if not.
    find_operands(eq_list, step)

        
find_operands(eq_list, step)   # calls the highest function from bidmas given - only 'dmas ATM
   