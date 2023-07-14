# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# Animal is a super class
class Animal:
    def __init__(self, birthType="", appearance="", blooded=""):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__, self.birthType, self.appearance, self.blooded)


# Mamal is a sub class
class Mamal(Animal):
        def __init__(self, birthType="born alive", appearance="hair or fur", blooded="warm blooded", nurseYoung=True):
            Animal.__init__(self, birthType, appearance, blooded)
            self.__nurseYoung = nurseYoung

        @property
        def nurseYoung(self):
            return self.__nurseYoung

        @nurseYoung.setter
        def nurseYoung(self, nurseYoung):
            self.__nurseYoung = nurseYoung

        def __str__(self):
            return super().__str__() + " and it is {} they nurse their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthType="born in an egg or born alive", appearance="dry scales", blooded="cold blooded",
                 nurseYoung=True):
        Animal.__init__(self, birthType, appearance, blooded)

    def sumAll(self, *args):
        sum = 0
        for n in args:
            sum += n
        return sum


def main():
    animal1 = Animal("born alive")
    print(animal1.birthType)
    print(animal1)
    print("----")

    mamal1 = Mamal()
    print(mamal1.birthType)
    print(mamal1.blooded)
    print(mamal1.appearance)
    print(mamal1.nurseYoung)
    print(mamal1)
    print("----")

    r1 = Reptile()
    print(r1.birthType)
    num = r1.sumAll(1, 2, 3, 4)
    print(num)
    print("----")


main()