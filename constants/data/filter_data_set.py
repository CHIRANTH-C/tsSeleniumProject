import datetime
class MyClass:
    def __init__(self):
        self._my_date = None  # Prefix with underscore to indicate it's a private attribute
        self._my_month = None  # Prefix with underscore to indicate it's a private attribute
        self._my_year = None  # Prefix with underscore to indicate it's a private attribute

        # Getter method
    def get_my_month(self):
        return self._my_month

        # Setter method
    def set_my_month(self, value):
        self._my_month = value

        # Getter method
    def get_my_date(self):
        return self._my_date

        # Setter method
    def set_my_date(self, value):
        self._my_date = value


        # Getter method
    def get_my_year(self):
        return self._my_year

        # Setter method
    def set_my_year(self, value):
        self._my_year = value

obj = MyClass()

current_date = datetime.datetime.now()
current_month = current_date.strftime("%B")
current_day = current_date.day
current_year = current_date.year

obj.set_my_date(current_day)
obj.set_my_month(current_month)
obj.set_my_year(current_year)

month , date , year = obj.get_my_month() , obj.get_my_date() , obj.get_my_year()

print(month , date , year)



