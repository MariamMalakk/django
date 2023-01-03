

class queue:
    def __init__(self):
        self.que = []

    def insert(self , que):
        self.que.append(que)

    def isEmpty(self, false=None):
        if len(self.que) == 0:
            return True
        else:
            return false


    def pop(self ):
        if self.isEmpty():
            return "the queue is empty!!"
        else:
            return self.que.pop(0)
    def display(self):
        for x in self.que:
            print(x)


q = queue()
q.insert(1)
q.insert(8)
q.display()
q.isEmpty()
q.pop()