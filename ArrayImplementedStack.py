Stack = []
p = 0 # p is for procedures
top = 0
Mtop = 0 # Mtop is max size of stack
while True:
    try:
        Mtop = int(input("How big would you like the stack to be?"))
        if Mtop > 0:
            break
        else:
            print("Please enter a valid integer.")
    except ValueError:
        continue
for i in range (Mtop):
    Stack.append(None)
def push(item):
    global top
    if is_full():
        print("Stack is full, cannot push item.")
    else:
        Stack[top] = item
        top += 1 
def pop():
    global top
    if is_empty() == True:
        print("Stack is empty nothing to pop")
    else:
        item = Stack[top-1]
        Stack[top-1] = None
        top -= 1
        return item
def is_empty():
    global top
    if top == 0:
        return True
    else:
        return False
def is_full():
    global top
    if top >= Mtop:
        return True
    else:
        return False
def peek():
    global top
    item = Stack[top-1]
    return item
def size():
    global top 
    return top
while True:
    p = input("1 is push, 2 is pop, 3 is peek, 4 is size, 5 is quit")
    try :
        p = int(p)
    except ValueError:
        print("Invalid input — please enter an integer.")
        continue
    if p == 1:
        item = input("What item would you like to push")
        push(item)
    elif p == 2:
        item = pop()
        if item == None:
            continue
        else:
            print(item , "has been popped")
    elif p == 3:
        item = peek()
        if item == None:
            print("Stack is empty nothing to peek")
        else:
            print(item , "is at the top of the list")
    elif p == 4:
        Size = size()
        print("The size of the stack is" , Size)
    elif p == 5:
        break
    else:
        print("Input not recognised please try again")   