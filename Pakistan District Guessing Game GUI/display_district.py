from turtle import Turtle


class DisplayDistrict:
    def __init__(self, x, y, district_name):
        """
        Initialize a DisplayDistrict object to display the district name on the map.
        """
        self.district_name = Turtle()
        self.district_name.penup()
        self.district_name.hideturtle()
        self.district_name.goto(x, y)
        self.__display_district_name(district_name)

    def __display_district_name(self, district_name):
        """
        Display the district name at the specified coordinates.
        """
        self.district_name.write(
            f"{district_name}", align="center", font=('Courier', 10, 'normal'))
