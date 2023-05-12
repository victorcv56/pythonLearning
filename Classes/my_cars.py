from car import Car
from electric_car import ElectricCar as EC

#create instance of non-electric car
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

#create instance of electric car
my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())