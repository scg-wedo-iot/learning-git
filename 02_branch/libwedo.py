import math

class MathOperate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        result = self.a + self.b
        return result

    def subtract(self):
	result = self.a - self.b
        return result
    
    def multipy(self):
	# Frame 
        pass
    
    def divde(self):
	# Nick
        pass

    def rms(self):
	# Frame
        pass
    
    def mean(self):
        pass

    def max(self):
        pass
    
    def min(self):
        pass

    def is_equal(self):
        pass
    
    def root_sum_sq(self):
        pass

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
