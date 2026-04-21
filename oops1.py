class Employee:
    def __init__(self):
        print("hi")
        self.id=1
        self.salary=10000
        self.designation="SE"
        print("welcome")
    def travel(self,destination):
        print("Sravan")
        print(destination)

sam=Employee()
print(sam.designation)
print(sam.id)
print(sam.salary)

sam.travel('kerala')
print(type(sam))
