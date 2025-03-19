# Euclidean algorithm for finding the greatest common divisor of two numbers
class euclidean_algorithm():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
    def GCD(self):
        while self.y !=0:
            self.x, self.y = self.y, self.x % self.y
        return self.x


