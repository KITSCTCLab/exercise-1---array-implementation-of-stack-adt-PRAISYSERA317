import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size
        self.top=-1

    def is_empty(self):
        # Write code here
        return self.top==-1

    def is_full(self):
        # Write code here
        return self.top==self.n-1

    def push(self, data):
        if not self.is_full():
            self.top+=1
            x=int(input("Enter data to be inserted: "))
            self.size[self.top]=x
            # Write code here

    def pop(self):
        if not self.is_empty():
            self.top=-1
            y=int(input("Enter data to be deleted: "))
            self.size[self.top]=y
            # Write code here

    def status(self):
        # Write code here
        for i in range(self.top+1):
            print(self.size[i])

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
