import math


class Rational:
    """Class for storing info about rational numbers in reduced form and performing basic arithmetic actions"""

    def __init__(self, *values):
        """Initialize a new instance and bring it to reduced form"""
        if values:
            if values[1] and isinstance(values[0], int) and isinstance(values[1], int):
                divisor = math.gcd(values[0], values[1])
                self.__numerator = values[0] // divisor
                self.__denominator = values[1] // divisor
            else:
                raise ValueError("Only integer values allowed! Second values is not zero.")
        else:
            self.__numerator = 1
            self.__denominator = 1

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def getfloat(self):
        return self.__numerator / self.__denominator

    def __add__(self, second):
        """Overloaded __add__ method for Rational class, accepts Rational instances and integers"""
        if isinstance(second, int):
            self.__numerator = self.__numerator + self.__denominator * second
        elif isinstance(second, Rational):
            self.__numerator = self.__numerator * second.__denominator + second.__numerator * self.__denominator
            self.__denominator = self.__denominator * second.__denominator
        else:
            raise TypeError("Add input should be integer or Rational!")
        return Rational(self.__numerator, self.__denominator)

    def __sub__(self, second):
        """Overloaded __sub__ method for Rational class, accepts Rational instances and integers"""
        if isinstance(second, int):
            self.__numerator = self.__numerator - self.__denominator * second
        elif isinstance(second, Rational):
            self.__numerator = self.__numerator * second.__denominator - second.__numerator * self.__denominator
            self.__denominator = self.__denominator * second.__denominator
        else:
            raise TypeError("Sub input should be integer or Rational!")
        return Rational(self.__numerator, self.__denominator)

    def __mul__(self, second):
        """Overloaded __mul__ method for Rational class, accepts Rational instances and integers"""
        if isinstance(second, int):
            self.__numerator = self.__numerator * second
        elif isinstance(second, Rational):
            self.__numerator = self.__numerator * second.__numerator
            self.__denominator = self.__denominator * second.__denominator
        else:
            raise TypeError("Mul input should be integer or Rational!")
        return Rational(self.__numerator, self.__denominator)

    def __truediv__(self, second):
        """Overloaded __truediv__ method for Rational class, accepts Rational instances and integers"""
        if isinstance(second, int):
            self.__numerator = self.__denominator * second
        elif isinstance(second, Rational):
            self.__numerator = self.__numerator * second.__denominator
            self.__denominator = self.__denominator * second.__numerator
        else:
            raise TypeError("Truediv input should be integer or Rational!")
        return Rational(self.__numerator, self.__denominator)

    def __eq__(self, second):
        """Overloaded equals method for Rational class, accepts Rational instances, integers and floats"""
        if isinstance(second, Rational):
            return self.getfloat() == second.getfloat()
        elif isinstance(second, (int, float)):
            return self.getfloat() == second
        else:
            return False

    def __lt__(self, second):
        """Overloaded less than method for Rational class, accepts Rational instances, integers and floats"""
        if isinstance(second, (int, float)):
            return self.getfloat() < second
        elif isinstance(second, Rational):
            return self.getfloat() < second.getfloat()
        else:
            raise TypeError("Only comparison with integers, floats and Rational allowed")

    def __gt__(self, second):
        """Overloaded greater than method for Rational class, accepts Rational instances, integers and floats"""
        if isinstance(second, (int, float)):
            return self.getfloat() > second
        elif isinstance(second, Rational):
            return self.getfloat() < second.getfloat()
        else:
            raise TypeError("Only comparison with integers, floats and Rational allowed")


def main():
    obj = Rational(2, 8)
    obj2 = Rational(3, 12)
    obj = obj + 2
    print(obj)
    obj = obj * obj2
    print(obj)
    print(obj == obj2)
    print(obj == 0.5625)
    print(obj < obj2)
    print(obj.getfloat())


if __name__ == '__main__':
    main()
