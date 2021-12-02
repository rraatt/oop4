from dataclasses import dataclass
# A dictionary, that  stores info about amount of days in a month
month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


@dataclass
class Days:
    """An auxiliary class for adding/subtracting days form a date"""
    value_calender: int


@dataclass
class Months:
    """An auxiliary class for adding/subtracting months form a date"""
    value_calender: int


@dataclass
class Years:
    """An auxiliary class for adding/subtracting years form a date"""
    value_calender: int


class Calendar:
    """A class for storing a date, constructor accepts 3 parameters of int type in the following order: day, month, year.
    It automatically checks if the date is correct and supports adding/ subtracting days/months/years form the date and
     comparison of date"""
    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    def is_leap(self):
        return not self.__year % 4 or not self.__year % 100 and not self.__year % 400

    def day_check(self, day):
        """A method for checking if current day is allowed to exist in current month and year"""
        days = month_days[self.__month]
        if self.__month == 2 and self.is_leap():
            days += 1
        return 1 <= day <= days

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError("Day should be an integer!")
        if not self.day_check(day):
            raise ValueError("Days value should be above zero, there should be enough days in selected month")
        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError("Month should be integer!")
        if not 1 <= month <= 12:
            raise ValueError("Month is above zero, there are twelve month!")
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Year should be an integer!")
        self.__year = year

    def __str__(self):
        return f'{self.__day}-{self.__month}-{self.__year}'

    def __iadd__(self, other):
        """Overloading __iadd__, input is an instance of Days, Years or Months dataclass
            if the value of instance is negative calls overloaded __isub__. Automatically brings the instance of
            Calendar to allowed form"""
        if other.value_calender < 0:
            other.value_calender = -other.value_calender
            return Calendar.__isub__(self, other)
        if isinstance(other, Years):
            self.__year += other.value_calender
        elif isinstance(other, Months):
            self.__month += other.value_calender
        elif isinstance(other, Days):
            self.__day += other.value_calender
        if self.__month > 12:
            self.__year += self.__month // 12
            self.__month = self.__month % 12
        while not self.day_check(self.__day):
            self.__day -= month_days[self.__month]
            if self.__month == 2 and self.is_leap():
                self.__day -= 1
            self.__month += 1
            if self.__month > 12:
                self.__year += 1
                self.__month -= 12
        return self

    def __isub__(self, other):
        """Overloading __isub__, input is an instance of Days, Years or Months dataclass
            if the value of instance is negative calls overloaded __iadd__. Automatically brings the instance of
             Calendar to allowed form"""
        if other.value_calender < 0:
            other.value_calender = -other.value_calender
            return Calendar.__iadd__(self, other)
        if isinstance(other, Years):
            self.__year -= other.value_calender
        elif isinstance(other, Months):
            self.__month -= other.value_calender
        elif isinstance(other, Days):
            self.__day -= other.value_calender
        if self.__month <= 0:
            self.__year -= self.__month // 12
            self.__month = self.__month % 12
        while not self.day_check(self.__day):
            self.__month -= 1
            self.__day += month_days[self.__month]
            if self.__month == 2 and self.is_leap():
                self.__day += 1
            if self.__month <= 0:
                self.__year -= 1
                self.__month += 12
        return self

    def __eq__(self, other):
        """Overloaded __eq__ for instances of Calendar class"""
        if not isinstance(other, Calendar):
            return False
        return self.__day == other.__day and self.__month == other.__month and self.__year == other.__year

    def __ne__(self, other):
        """Overloaded not equals for Calendar class"""
        return not Calendar.__eq__(self, other)

    def __lt__(self, other):
        """Overloaded less than for Calendar class"""
        if not isinstance(other, Calendar):
            raise TypeError("Only comparison with Calendar allowed")
        if not self.__year == other.__year:
            return self.__year < other.__year
        if not self.__month == other.__month:
            return self.__month < other.__month
        if not self.__day == other.__day:
            return self.__day < other.__day
        return False

    def __le__(self, other):
        """Overloaded less or equals for Calendar class"""
        if not isinstance(other, Calendar):
            raise TypeError("Only comparison with Calendar allowed")
        if not self.__year == other.__year:
            return self.__year < other.__year
        if not self.__month == other.__month:
            return self.__month < other.__month
        if not self.__day == other.__day:
            return self.__day < other.__day
        return True

    def __gt__(self, other):
        """Overloaded greater than for Calendar class"""
        if not isinstance(other, Calendar):
            raise TypeError("Only comparison with Calendar allowed")
        if not self.__year == other.__year:
            return self.__year > other.__year
        if not self.__month == other.__month:
            return self.__month > other.__month
        if not self.__day == other.__day:
            return self.__day > other.__day
        return False

    def __ge__(self, other):
        """Overloaded greater or equals for Calendar class"""
        if not isinstance(other, Calendar):
            raise TypeError("Only comparison with Calendar allowed")
        if not self.__year == other.__year:
            return self.__year > other.__year
        if not self.__month == other.__month:
            return self.__month > other.__month
        if not self.__day == other.__day:
            return self.__day > other.__day
        return True


def main():
    obj = Calendar(29, 2, 2020)
    obj2 = Calendar(29, 2, 2020)
    print(obj == obj2)
    #obj2 += Days(50)
    #print(obj2)
    obj2 += Months(24)
    print(obj2)
    print(obj >= obj2)


if __name__ == '__main__':
    main()
