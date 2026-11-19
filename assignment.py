# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = []
TopOfStack = -1
for i in range(8):
    Stack.append(-1)


def Push(Item):
    global TopOfStack
    if TopOfStack == 7:
        return False
    TopOfStack += 1
    Stack[TopOfStack] = Item
    return True


def Pop():
    global TopOfStack
    if TopOfStack == -1:
        return -1
    Item = Stack[TopOfStack]
    TopOfStack -= 1
    return Item


# Exercise 2
def ShowStack():
    if TopOfStack == -1:
        return ""
    items = []
    for i in range(TopOfStack, -1, -1):
        items.append(str(Stack[i]))
    return " ".join(items)


# Exercise 3
def DecimalToBinary(Number):
    global TopOfStack
    TopOfStack = -1
    if Number == 0:
        return "0"
    while Number > 0:
        Push(Number % 2)
        Number = Number // 2
    binary = ""
    while TopOfStack != -1:
        binary += str(Pop())
    return binary


# Exercise 4
def Editor(Commands):
    global TopOfStack
    TopOfStack = -1
    for cmd in Commands:
        if cmd == "undo":
            Pop()
        else:
            letter = cmd.split(" ")[1]
            Push(letter)
    text = ""
    for i in range(TopOfStack + 1):
        text += Stack[i]
    return text
