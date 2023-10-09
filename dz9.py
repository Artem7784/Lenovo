class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def create_person(cls, name, birth_year, gender):
        age = cls.calculate_age(birth_year)
        return cls(name, age, gender)

    @staticmethod
    def calculate_age(birth_year):
        current_year = 2023
        return current_year - birth_year

person1 = Person("Alice", 30, "Female")

person1.display_info()

person2 = Person.create_person("Bob", 1985, "Male")

person2.display_info()




#
#
#
# class MyMetaClass(type):
#     def __new__(cls, name, bases, class_dict):
#
#         new_class = super().__new__(cls, name, bases, class_dict)
#         return new_class
#
# class MyClass(metaclass=MyMetaClass):
#     class_variable = "I am a class variable"
#
#     def __init__(self, data):
#         self.data = data
#
#
# # Создание экземпляра класса
# obj = MyClass("Hello, World!")
#
# print(obj.data)
#
# print(MyClass.class_variable)
