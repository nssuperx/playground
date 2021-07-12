from enum import Enum, auto

class testClass():
    element1 = 1
    element2 = "string"

    def instanceMethod(self):
        pass

    @classmethod
    def classMethod():
        pass

    @staticmethod
    def staticMethod():
        pass


class enumClass(Enum):
    cpu = auto()
    memory = auto()
    motherboard = auto()

def main():
    test = testClass()
    print("instantiate")
    print(test.element1)
    print(test.element2)

    print("static")
    print(testClass.element1)
    print(testClass.element2)

    print("enum")
    check_part(enumClass.cpu)

def check_part(part):
    if part == enumClass.cpu:
        print("cpu")
    else:
        print("not cpu")


if __name__ == '__main__':
    main()
