class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + self.b

    def __sub__(self, other):
        return self.a - self.b

    def __mul__(self, other):
        return self.a * self.b

    def __truediv__(self, other):
        return self.a / self.b

a = Math(10, 3)

print(a + a)
print(a - a)
print(a * a)
print(a / a)