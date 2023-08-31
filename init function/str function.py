class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.age})"    

p1 = person("Antony", 25)
print(p1)     