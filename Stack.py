class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, new_item):
        self.items.append(new_item)

    def pop(self):
        swap = self.items[len(self.items)-1]
        self.items.remove(swap)
        return swap

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []


