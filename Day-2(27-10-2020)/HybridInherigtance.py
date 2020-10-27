class Parent:
    def fun1():
        return "i am from Parent Class"

class Child(Parent):
    def fun2():
        return "i am from Child class"

class Child1(Parent):
    def fun3():
        return "i am from Child1 Class"

class Child2(Child,Child1):
    def fun4():
        return "i am from Child2 Class"
