import time
from threading import Thread


def car(speed, pilot):
    dist = 0
    while dist <= 100:
        dist += speed
        time.sleep(0.5)
        print("Pilot: {} km: {}".format(pilot, dist))


t_car1 = Thread(target=car, args=[1, 'Gary'])
t_car2 = Thread(target=car, args=[2, 'Mark'])

t_car1.start()
t_car2.start()
