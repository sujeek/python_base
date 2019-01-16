class Singleton:
    instance = None

    @staticmethod
    def get_instance():
        if Singleton.instance == None:
            Singleton()
        return Singleton.instance

    def __init__(self):
        if Singleton.instance != None:
            raise Exception("This class is a singleton!")
        Singleton.instance = self

s = Singleton()
print(s)

s = Singleton.get_instance()
print(s)

s = Singleton.get_instance()
print(s)