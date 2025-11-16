class v:
    def __init__(self, name, max_speed, mileage):
        self.name= name
        self.max_speed= max_speed
        self.mileage= mileage

o1=v("Lamborghini", 320, 29)
print(o1.name, o1.max_speed, o1.mileage)
o2=v("Bugatti", 350, 26)
print(o2.name, o2.max_speed, o2.mileage)
o3=v("Ferrari", 310, 30)
print(o3.name, o3.max_speed, o3.mileage)