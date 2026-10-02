def Stack():
    stack = []
    max_size = 6
    print(stack)

    if len(stack) < max_size:
        stack.append(15)
    print(stack)

    if len(stack) < max_size:
        stack.append(25)
    print(stack)

    if len(stack) < max_size:
        stack.append(35)
    print(stack)

    if len(stack) < max_size:
        removed = stack.pop()
        print("Reoved Element: ",removed)
    print(stack)

    if len(stack) < max_size:
        stack.append(45)
    print(stack)

    if len(stack) < max_size:
        stack.append(55)
    print(stack)

    print("Top Element: ",stack[-1])

    if len(stack) < max_size:
        removed = stack.pop()
        print("Popped element: ",removed)
    print(stack)

    if len(stack) < max_size:
        stack.append(65)
    print(stack)



def compare():
    stack1 = [12,25,38,41,56]
    stack2 = [12,25,38,41,60]

    while len(stack1) > 0:
        
        print("\n")
        print("Stack 1 : ",stack1)
        print("Stack 2 : ",stack2)
        print("\n")

        stack1Rem = stack1.pop()
        stack2Rem = stack2.pop()
        
        if stack1Rem < stack2Rem:
            print("Stack 1 popped element is smaller than Stack 2 popped element")
        elif stack1Rem == stack2Rem:
            print("Stack 1 popped element is equal for Stack 2 popped element")
        else:
            print("Stack 1 popped element is bigger than Stack 2 popped element")




def queue():
    queue = []
    max_size = 6

    if len(queue) < max_size:
        queue.append(5)
    print("ENQUEU(5): ",queue)

    if len(queue) < max_size:
        queue.append(15)
    print("ENQUEU(15): ",queue)

    if len(queue) < max_size:
        queue.append(25)
    print("ENQUEU(25): ",queue)

    if len(queue) < max_size:
        removed = queue.pop()
        print("Reoved Element: ",removed)
    print("DEQUEU(): ",queue)

    if len(queue) < max_size:
        queue.append(35)
    print("ENQUEU(35): ",queue)

    if len(queue) < max_size:
        queue.append(45)
    print("ENQUEU(45): ",queue)

    if len(queue) < max_size:
        removed = queue.pop()
        print("Reoved Element: ",removed)
    print("DEQUEU(): ",queue)

    if len(queue) < max_size:
        queue.append(55)
    print("ENQUEU(55): ",queue)

    print("Top Element: ",queue[0])

    if len(queue) < max_size:
        queue.append(65)
    print(queue)

queue()