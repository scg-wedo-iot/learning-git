import math

class MathOperate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        result = self.a + self.b
        return result

    def subtract(self):
        # O
<<<<<<< HEAD
        return None

=======
        result = self.a - self.b
        return result
    
>>>>>>> feat-sub-min
    def multipy(self):
        # Book
        result = self.a * self.b
        return result
    
    def divde(self):
        if (self.b != 0):
            result = self.a / self.b
        else:
            result = "Can not use dinominator value = 0"
        return result

    def rms(self):
        # pond
        result = math.sqrt((pow(self.a,2)+pow(self.b,2))/2)
        return result
    
    def mean(self):
        # gear
        return self.sum()/2

    def max(self):
        # Park
        data = [self.a,self.b]
        return max(data)
    
    def min(self):
<<<<<<< HEAD
        if self.a <= self.b:
            result = self.a
        
        else:
            result = self.b

        return result

=======
        if self.a>self.b :
            return self.b
        return self.a
    
>>>>>>> feat-sub-min
    def is_equal(self):
        # Kuang
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
