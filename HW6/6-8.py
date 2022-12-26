class Point:
    def __init__(
            self,
            x: float,
            y: float
    ):
        self.set_xy(x, y)

    def set_xy(self, x: float, y: float):
            self.__x = x
            self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Rectangle:

    def __init__(
            self,
            point1: Point,
            point2: Point

    ):
        self.set_points(point1, point2)

    def set_points(self, Point1, Point2):
        if isinstance(Point1, Point) and isinstance(Point2, Point):
            self.__Point1 = Point1
            self.__Point2 = Point2

    def get_perimeter(self):
        return 2*(self.__Point2.get_y() - self.__Point1.get_y() + self.__Point2.get_x() - self.__Point1.get_x())

    def get_area(self):
        return (self.__Point2.get_y() - self.__Point1.get_y()) * (self.__Point2.get_x() - self.__Point1.get_x())

    def contains(self, pointcheck: Point):
        if (self.__Point1.get_x() <= pointcheck.get_x() <= self.__Point2.get_x()) and (self.__Point1.get_y() <= pointcheck.get_y() <= self.__Point2.get_y()):
            return True
        else:
            return False


b = Rectangle(Point(0,0), Point(2,2))
print(b.get_perimeter())
print(b.get_area())
print(b.contains(Point(2, 2)))
