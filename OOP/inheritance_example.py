class Vehicle:
    def start(self):
        raise NotImplementedError('Implement the abstract method')

    def drive(self):
        raise NotImplementedError('Implement the abstract method')

    def stop(self):
        raise NotImplementedError('Implement the abstract method')


class Cycle(Vehicle):

    def start(self):
        print('Unlock and sit on the cycle.')

    def drive(self):
        print('Do pedalling and apply right direction.')

    def stop(self):
        print('Stop pedalling and apply breaks to stop.')


class Car(Vehicle):

    def start(self):
        print('Unlock and start the car engine.')

    def drive(self):
        print('Apply right gears with clutch and accelerator combination.')

    def stop(self):
        print('Press clutch and shift down the gears and apply break to stop the car.')


def operate_vehicle(vehicle):
    vehicle.start()
    vehicle.drive()
    vehicle.stop()


def main():
    cycle = Cycle()
    car = Car()
    print('#' * 100)
    print('Operate Cycle')
    operate_vehicle(cycle)
    print('#' * 100)
    print('Operate Car')
    operate_vehicle(car)
    print('#' * 100)


if __name__ == '__main__':
    main()
