import math
# Perimeter


def _init_(self) -> None:
    pass

# second function
    def PeriRectangle(self):
        l = int(input("Enter Lenght:\n"))
        w = int(input("Enter Width: \n"))
        p = l + w + l + w
        print("Perimeter is: ", p, " cm")

# third function
    def PeriSquare(self):
        s = int(input("enter side:\n"))
        p = s + s + s + s
        print("perimeter of square is: ", p, " cm")


# Fourth function - triangle


    def PeriTriangle(self):
        s = int(input("enter side:\n"))
        p = s + s + s
        print("Perimeter of Triangle is: ", p, " cm")

# Fifth function - circle
    def CCircumference(self):
        r = int(input("Enter radius: \n"))
        c = 2 * math.pi * r
        print("circumference of circle is: ", c, " cm")


# initialising objects
print("Welcome to the Perimeter Box\n")
print("choose which object to calculate its perimeter\n")
choice = int(input("1.Rectangle\n2.Square\n3.Triangle\n4.Circle"))
