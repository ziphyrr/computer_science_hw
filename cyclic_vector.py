DEF_ELEMENT = 0

class CyclicVector():
    def __init__ (self, capacity = 1):
        self.head = 0
        self.tail = 0
        self.capacity = capacity
        self.elements = [DEF_ELEMENT] * capacity

    def get(self, i):
        if (
            (self.head == self.tail) 
            or (self.head < self.tail and (i < self.head or i >= self.tail)) 
            or (self.head > self.tail and (i < self.head and i >= self.tail))
        ):
            return None
        return self.elements[i]

