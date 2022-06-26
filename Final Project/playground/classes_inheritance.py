instances_dict = {}


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if type(self) is Foo:
            instances_dict[name] = age

class Bar(Foo):
    def __init__(self,name, age ):
        super().__init__(name, age)


Foo("Alex", 35)
Foo("Amnda", 35)
print(instances_dict)   
Bar("Aron", 35)
print(instances_dict)