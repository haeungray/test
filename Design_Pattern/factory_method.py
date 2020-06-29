from abc import ABCMeta, abstractclassmethod


class Animal(metaclass = ABCMeta):
    def do_say(self):pass

class Doc(Animal):
    def do_say(self):
        print("bow bow")


class Cat(Animal):
    def do_say(self):
        print("MEOWMEOW")

class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

if __name__ == '__main__':
    ff = ForestFactory()
    animal = input('Doc or Cat?')
    ff.make_sound(animal)