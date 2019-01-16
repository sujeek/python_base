
class Stack:
    def __init__(self):
        self.stack  = []

    def posh(self, data):
        if data is not None:
            self.stack.append(data)
            return True
        return False

    def peek(self):
        return self.stack[0]

    def length(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack)<=0:
            return "No element in the Stack!"
        return self.stack.pop()