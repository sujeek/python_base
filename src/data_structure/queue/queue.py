
class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        if data is not None:
            self.queue.insert(0,data)
            return True
        return False

    def size(self):
        return len(self.queue)

    def pop(self):
        if len(self.queue) <=0:
            return "No element in the Queue!"
        return self.queue.pop()
