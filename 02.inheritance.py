"""How to implement inheritance."""


class Talker(object):

    def __init__(self, skills=0):
        self.skills = skills

    def say_hi(self):
        base = "%s: " % self
        if self.skills <= 0:
            print(base + "...")
        elif 0 < self.skills < 10:
            print(base + "hi !")
        else:
            print(base + "Hello you !")

    def __str__(self):
        return self.__class__.__name__


class Person(Talker):
    def __init__(self, name):
        super().__init__(skills=10)
        self.name = name

    def __str__(self):
        return self.name


class Robot(Talker):
    def __init__(self, identity):
        super().__init__(skills=5)
        self.id = identity

    def say_hi(self):
        print("/!\\ A robot is talking:")
        super().say_hi()

    def __str__(self):
        return "<%s>" % self.id


if __name__ == "__main__":
    talker = Talker()
    person = Person("Mike")
    robot = Robot("m1r0b0t")
    talker.say_hi()
    print()
    person.say_hi()
    print()
    robot.say_hi()
