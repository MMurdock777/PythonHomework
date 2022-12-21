class Clock:

    def __init__(
            self,
    ):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def set_time(self, hours: int, minutes: int, seconds: int):
        if isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
            if hours < 0 or minutes < 0 or seconds < 0 or hours > 23 or minutes > 59 or seconds > 59:
                print("Часы задаются в диапозоне 0-23, минуты/секунды - 0-59.")
            else:
                self.hours = hours
                self.minutes = minutes
                self.seconds = seconds
        else:
            print("Заданные значения не числового типа")

    def get_time(self):
        out_seconds = str(self.seconds)
        out_minutes = str(self.minutes)
        out_hours = str(self.hours)
        if len(out_seconds) < 2:
            out_seconds = "0" + out_seconds
        if len(out_minutes) < 2:
            out_minutes = "0" + out_minutes
        if len(out_hours) < 2:
            out_hours = "0" + out_hours

        return f"{out_hours}:{out_minutes}:{out_seconds}"

    def add_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.add_minute()

    def add_minute(self):
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.add_hour()

    def add_hour(self):
        self.hours += 1
        if self.hours == 24:
            self.hours = 0

    def __add__(self, other):
        new_clock = Clock()
        new_clock.set_time(self.hours, self.minutes, self.seconds)
        for i in range(other.seconds):
            new_clock.add_second()
        for i in range(other.minutes):
            new_clock.add_minute()
        for i in range(other.hours):
            new_clock.add_hour()
        return new_clock


a = Clock()
a.set_time(21, 59, 0)
print(a.get_time())
a.add_minute()
print(a.get_time())
b = Clock()
b.set_time(2, 3, 1)
c = a + b
print(c.get_time())
