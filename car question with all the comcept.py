        
class Car:
    def __init__(self, name, rent, status):
        self.name = name
        self.rent = rent
        self.status = status


def create_car(name, rent, status):
    return Car(name, rent, status)


cars = []


cars.append(create_car("toyota ", 300, "Available"))
cars.append(create_car("honda civic", 250, "Available"))
cars.append(create_car("ford mustang", 500, "Available"))
cars.append(create_car("ferrari s200", 700, "Available"))

for car in cars:
    print(f"Car: {car.name} | Rent per Hour: rs{car.rent}| Status: {car.status}")
user=input("enter car name from above option :" )


for i in enumerate(cars):
   
    if user.lower()=="toyota":
        rent=int(input("how many hours you want to rent the car : " ))
        total=(cars[0].rent*rent)
        print("total rent will be : rs",total)
        cars[0].status="unavailable"
        print(f" Status: {i.status}")
        break
        
    elif user.lower()=="honda civic":
        rent=int(input("how many hours you want to rent the car : " ))
        total=(cars[1].rent*rent)
        print("total rent will be : rs",total)
        cars[1].status="unavailable"
        print(f" Status: {i.status}")
        break
    
    elif user.lower()=="ford mustang":
        rent=int(input("how many hours you want to rent the car : " ))
        total=(cars[2].rent*rent)
        print("total rent will be : rs",total)
        cars[2].status="unavailable"
        print(f" Status: {i.status}")
        break
    
    elif user.lower()=="ferrari s250":
        rent=int(input("how many hours you want to rent the car : " ))
        total=(cars[3].rent*rent)
        print("total rent will be : rs",total)
        cars[3].status="unavailable"
        print(f" Status: {i.status}")
        break
    
        

