DEF_ELEMENT = 0

class CyclicVector():
    def __init__ (self, capacity = 1):
        self.head = 0
        self.tail = 0
        self.capacity = capacity
        self.elements = [DEF_ELEMENT] * capacity

