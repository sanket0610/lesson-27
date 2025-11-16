class P:
    s="bird"
    def __init__(self, name, age):
        self.name= name
        self.age= age

blu=P("Blu", 10)
Woo=P("Woo", 15)

print("Blu is a {}".format(blu.s))
print("Woo is also a {}".format(Woo.s))

print("{} IS {} YEARS OLD". format(blu.name, blu.age))
print("{} IS {} YEARS OLD". format(Woo.name, Woo.age))