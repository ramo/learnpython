from OOP.class_example import Rocket


class RocketLauncher:
    def __init__(self, rocket):
        self.__rocket = rocket

    def launch(self):
        print('Launching:', self.__rocket.get_name())


if __name__ == '__main__':
    r = Rocket('ISRO-123')
    launcher = RocketLauncher(r)
    launcher.launch()
