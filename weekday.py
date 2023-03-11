class WeekDayError(Exception):
    pass


class Weeker:
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.day = Weeker.days.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.days[self.day]

    def add_days(self, n):
        self.day = (self.day + n) % 7

    def subtract_days(self, n):
        self.add_days(-n)


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
