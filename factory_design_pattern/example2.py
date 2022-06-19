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

    def __init__(self):
        self._persons = {}

    def register_user_type(self, person_type, person):
        self._persons[person_type] = person

    def get_description(self, person_type):
        person = self._persons.get(person_type)
        if not person:
            raise ValueError(person_type)
        return person()


if __name__ == "__main__":
    factory = PersonFactory()
    factory.register_user_type("student", Student)
    factory.register_user_type("employee", Employee)
    choice = input("Enter student or employee: ")
    factory.get_description(choice).person_method()
