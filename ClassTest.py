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
        # 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，
        # 并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
        # 不是private变量，所以，不能用__name__、__score__这样的变量名。
        #
        # 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，
        # 这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
        # 当你看到这样的变量时，意思就是，“虽然我可以被访问，
        # 但是，请把我视为私有变量，不要随意访问”。
        #
        # 双下划线开头的实例变量是不是一定不能从外部访问呢？
        # 其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
        # 所以，仍然可以通过_Student__name来访问__name变量

    def print_score(self):
        print("%s : %s\n" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        # 参数检查
        if 0 <= new_score <= 100:
            self.__score = new_score
        else:
            raise ValueError("Wrong score!")


# 继承和多态
class Animal(object):

    def __init__(self, name="Animal"):
        self.__name = name

    def run(self):
        print("%s is running" % self.__name)

    def getName(self):
        return self.__name


class Dog(Animal):
    def run(self):
        print("Dog %s is running" % self.getName())


if __name__ == '__main__':
    tom = Human("Tom", "boy", 10)
    tom.SayHi()
    del tom

    jerry = Student("Jerry", 90)
    jerry.print_score()
    # jerry.set_score(999)
    del jerry

    snoopy = Dog("Snoopy")
    snoopy.run()

    # student = Student("Ding")
    # student.Read()
    # del student
