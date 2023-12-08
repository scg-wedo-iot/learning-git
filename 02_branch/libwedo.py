import math

class MathOperate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):
        result = self.a + self.b
        return result
    
    def subtract(self):
        return None
    
    def multipy(self):
        return None
    
    def divde(self):
        return None

    def rms(self):
        return None
    
    def mean(self):
        return None
    
    def max(self):
        return None
    
    def min(self):
        return None
    
    def is_equal(self):
        return None
    
    def root_sum_sq(self):
        return None

    def show_result(self):
        print(f"a: {self.a}, b: {self.b}")
        print(f"sum: {self.sum()}")
        print(f"subtract: {self.subtract()}")
        print(f"multiply: {self.multipy()}")
        print(f"divide: {self.divde()}")
        print(f"rms: {self.rms()}")
        print(f"mean: {self.mean()}")
        print(f"max: {self.max()}")
        print(f"min: {self.min()}")
        print(f"is_equal: {self.is_equal()}")
        print(f"root_sum_sq: {self.root_sum_sq()}")
            