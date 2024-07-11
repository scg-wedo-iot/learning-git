import math

class MathOperate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        result = self.a + self.b
        return result

    def subtract(self):
	#Shung
        result = self.a - self.b
        return result
    
    def multipy(self):
        result = self.a * self.b
        return result
    
    def divide(self):
        # Nick
        result = self.a / self.b
        return result
        pass

    def rms(self):
        result = math.sqrt((math.pow(self.a, 2) + math.pow(self.b, 2))/2)
        return result
    
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
        print(f"divide: {self.divide()}")
        print(f"rms: {self.rms()}")
        print(f"mean: {self.mean()}")
        print(f"max: {self.max()}")
        print(f"min: {self.min()}")
        print(f"is_equal: {self.is_equal()}")
        print(f"root_sum_sq: {self.root_sum_sq()}")
