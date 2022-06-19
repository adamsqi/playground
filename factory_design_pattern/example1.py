from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self):
        """ Interface for person_method """


class Student(IPerson):

    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("I am a student")


class Employee(IPerson):

    def __init__(self):
        self.name = "Basic employee name"

    def person_method(self):
        print("I am an employee")


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "student":
            return Student().person_method()
        if person_type == "employee":
            return Employee().person_method()
        print("Invalid type")
        return -1


if __name__ == "__main__":
    choice = input("Enter student or employee: ")
    PersonFactory.build_person(person_type=choice)
