# 类的定义与使用
class Human(object):
    name = "no name"

    def __init__(self, name="no one"):
        self.name = name

    def __del__(self):
        print("I, %s, am destroyed" % self.name)

    def SayName(self):
        print("My name is %s" % self.name)

# 类的继承
class Student(Human):

    def Read(self):
        print("%s is reading" % self.name)


if __name__ == '__main__':
    tom = Human("Tom")
    tom.SayName()
    # tom.__del__()
    del tom

    jerry = Human()
    jerry.SayName()
    # jerry.__del__()
    del jerry

    student = Student("Ding")
    student.Read()
    del student
