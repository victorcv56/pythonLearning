from Restaurant import Restaurant as r
from IceCreamStand import IceCreamStand as IC

my_restaurant = r('Delicioso', 'mexican')
my_restaurant.describe_restaurant()

my_stand = IC('Lickin', 'ice cream')
my_stand.describe_restaurant()
my_stand.open_restaurant()