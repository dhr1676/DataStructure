# 类的定义
class Human(object):
    # 实例的变量名以"__"开头，则变为私有变量
    def __init__(self, name="no one", gender="Unknown", age=0):
        self.__name = name
        self.__gender = gender
        self.age = age

    def __del__(self):
        print("I, %s, am destroyed\n" % self.__name)

    def SayHi(self):
        print("My name is %s, my gender is %s \n" % (self.__name, self.__gender))


# 类的定义与使用
class Student(object):

    def __init__(self, name="no one", score=0):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s : %s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score
        else:
            raise ValueError("Wrong score!")


if __name__ == '__main__':
    tom = Human("Tom", "boy", 10)
    tom.SayHi()
    del tom

    jerry = Student("Jerry", 90)
    jerry.print_score()
    # jerry.set_score(999)
    del jerry

    # student = Student("Ding")
    # student.Read()
    # del student
