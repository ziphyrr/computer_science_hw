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

    def size(self): # random comment
        return (self.capacity - self.head + self.tail) % self.capacity

    def add(self, x):
        if self.size() + 2 > self.capacity:
            self.change_capacity(True)
        self.elements[self.tail] = x
        if self.tail == self.capacity - 1:
            self.tail = 0
        else:
            self.tail += 1

    def erase_first(self):
        if 4 * self.size() <= self.capacity:
            self.change_capacity(False)
        if self.head == self.capacity - 1:
            self.head = 0
        else:
            self.head += 1

    def change_capacity(self, increase_flg):
        if increase_flg == True:
            new_elements = [DEF_ELEMENT] * (self.capacity * 2)
        else:
            new_elements = [DEF_ELEMENT] * (self.capacity // 2)
        for i in range(self.size()):
            new_elements[i] = self.elements[(self.head + i) % (self.capacity)]
        
        self.tail = self.size()
        self.head = 0
        self.elements = new_elements
        self.capacity = self.capacity * 2 if increase_flg == True else self.capacity // 2

