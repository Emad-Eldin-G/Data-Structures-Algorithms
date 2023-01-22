from math import pi

class _Shape:
    def __init__(self, sides, name):
        self._sides = sides
        self._name  = name

    def is_polygon(self):
        return True
    

class Circle(_Shape):
    def __init__(self, sides, name, radius):
        super().__init__(sides, name)
        self._radius = radius

    def is_polygon(self):
        return False

    def get_radius(self):
        return self._radius

    def area(self):
        return round(pi * (self._radius * self._radius), 1)


class Triangle(_Shape):
    def __init__(self, sides, name, angle_1, angle_2, angle_3):
        super().__init__(sides, name)
        self._angle_1 = angle_1
        self._angle_2 = angle_2
        self._angle_3 = angle_3

    def is_right_angle(self):
        angles = [self._angle_1, self._angle_2, self._angle_3]
        if 90 in angles:
            return True 
        return False

class Square(_Shape):
    def __init__(self, sides, name, side):
        super().__init__(sides, name)
        self.__side_length = side

    def area(self):
        return (self.__side_length**2)


# Test Cases:
t1 = Triangle('MyTriangle', 3, 85, 50, 45)
print(t1.is_polygon()) # Should return True
print(t1.is_right_angle()) # Should return True

c1 = Circle('MyCircle', 0, 5)
print(c1.is_polygon()) # Should return False
print(c1.area())

s1= Square('MySquare', 4, 5)
print(s1.area())
