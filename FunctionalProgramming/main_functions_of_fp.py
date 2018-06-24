import random
from functools import reduce


class Student:
    def __init__(self, name, age, dep):
        self.__name = name
        self.__age = age
        self.__dep = dep

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_department(self):
        return self.__dep

    def __str__(self):
        return 'Student: name = {0}, age = {1}, department = {2}'.format(self.__name, self.__age, self.__dep)


def populate_students(n):
    students = []
    for _ in range(n):
        name = ''.join([chr(65 + random.randint(0, 25)) for _ in range(random.randint(5, 10))])
        age = random.randint(17, 22)
        dep = random.choice(['ECE', 'MECH', 'CSC', 'IT', 'E&I', 'EEE'])
        students.append(Student(name, age, dep))
    return students


def main():
    students = populate_students(10)
    print('#' * 50)
    print('Student list')
    print('#' * 50)
    for s in students:
        print(s)
    print('#' * 50)

    # map test
    names = list(map(lambda x: x.get_name(), students))
    print('Student names:', names)

    # filter test
    majors = list(map(lambda x: (x.get_name(), x.get_age()), filter(lambda x: x.get_age() >= 18, students)))
    print('Major students:', majors)

    # reduce test
    total_age = reduce(lambda x, y: x + y, map(lambda x: x.get_age(), students))
    print('Average age of students:', total_age / len(students))


if __name__ == '__main__':
    main()
