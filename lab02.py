# Lab 2: Calculator

current_value = 0
operations = []



# Lab 3 

def get_current_value():
    pass


# Problem 2:
def display_current_value():
    global current_value
    print("Current value: " + str(current_value))


def add_to_operations():
    global current_value, operations
    operations.append(current_value)
    if len(operations) >= 3:
        del operations[0]

# Problem 3: Addition
def add(to_add):
    global current_value, operations
    # global is used to update the current_value,
    # if not used, the updates would only be local to this function
    current_value += to_add
    add_to_operations()

def subtract(to_subtract):
    global current_value, operations
    current_value -= to_subtract
    add_to_operations()

# Problem 5: Multiplication and Division
def mult(to_multiply):
    global current_value, operations
    current_value *= to_multiply
    add_to_operations()

def divide(to_divide):
    global current_value, operations
    if (to_divide != 0):
        current_value /= to_divide
    add_to_operations()

# Problems with the division function:
#   It may lead to floats that are imprecise

saved = ""
# Problem 6: Memory and Recall 
def memory():
    # saves the current value
    global current_value, saved
    saved = str(current_value)


def recall():
    # restores the saved value
    global current_value, saved
    current_value = int(saved)
    

# Problem 7: Undo
def undo():
    """restores the previous value that appeared on screen 
    before the current value"""

    # pressing undo twice restores the original value 
    global current_value, operations
 
    # solution: since there are only 2 values stored, swap
    operations[0], operations[1] = operations[1], operations[0]
    current_value = operations[-1]

# global variable representing the current file as main 
if __name__ == "__main__":
    print("Welcome to the calculator program")

    

    display_current_value() # 0
    add(5) # 5
    subtract(2) 
    display_current_value() # 3
    undo() 
    display_current_value() # 5
    undo() 
    display_current_value() # 3
    mult(10)
    display_current_value() # 30
    undo() 
    undo() 
    display_current_value() # 30
    undo() 
    undo() 
    undo() 
    display_current_value() # 3

