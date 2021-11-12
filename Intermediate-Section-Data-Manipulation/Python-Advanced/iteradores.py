# %%
import time

class FiboIter():
    
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        if self.n2 > self.max:
            raise StopIteration
        elif self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
# %%
fibonacci = FiboIter(10000000000000000000000000)
for element in fibonacci:
    print(element)
# %%
