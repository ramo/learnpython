class Rocket:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == '__main__':
    r = Rocket('ISRO-123')
    print(r.get_name())
