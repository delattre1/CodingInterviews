# DO NOT CHANGE THIS CLASS
class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


# IMPLEMENT YOUR SOLUTION HERE (DO NOT CHANGE THE ARGUMENTS)
def sort_stack(stack: Stack) -> None:
    tmp_stack = Stack()
    
    while not stack.is_empty():
        tmp = stack.pop()

        while (not tmp_stack.is_empty()) and (tmp_stack.peek() > tmp):
            stack.push(tmp_stack.pop())
        
        tmp_stack.push(tmp)

    while not tmp_stack.is_empty():
        stack.push(tmp_stack.pop())

    
