# takes a string from the user and splits this into a list
equation = input("Please input the equation you would like to step through. \n")
eq_list = equation.split(" ")


def run(eq_list):
    """loop over the list and add or subtract the numbers,  then add back to list and 
        remove the adjacent values"""
    n = None
    for n in range(len(eq_list)):
        if eq_list[n] == "+":
            n = n
            print("Step: ", eq_list[n-1], " + ", eq_list[n+1])
            temp = int(eq_list[n-1]) + int(eq_list[n+1])
            eq_list[n] = temp
            break
    del eq_list[n+1]
    del eq_list[n-1]
    print(eq_list)
    
    if len(eq_list) > 1:
        run(eq_list)

run(eq_list)       