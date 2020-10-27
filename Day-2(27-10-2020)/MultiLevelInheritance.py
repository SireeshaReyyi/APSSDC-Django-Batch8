class ClassA:
    a=20
    def A():
        return "I am from ClassA"

class ClassB(ClassA):
    b=30
    def B():
        return "I am from ClassB"

class ClassC(ClassB):
    c=40
    def C():
        return "I am from ClassC"
    
