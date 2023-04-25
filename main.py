class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print("Meow!")

    def info(self):
        print(f"Name: {self.name}, Age: {self.age} years old")

cat1 = Cat("Neko", 3)
cat2 = Cat("Kito", 5)


cat1.meow()
cat1.info() 

cat2.meow() 
cat2.info()