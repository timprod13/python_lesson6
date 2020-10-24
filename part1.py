from time import sleep
import random


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    @staticmethod
    def running():
        i = 0
        i_rand = 0
        while i == i_rand:
            print("Traffic light turns ")
            if i == 0:
                print(f"{TrafficLight.__color[i]}")
                sleep(7)
                i += 1
            elif i == 1:
                print(f"{TrafficLight.__color[i]}")
                sleep(2)
                i += 1
            elif i == 2:
                print(f"{TrafficLight.__color[i]}")
                sleep(5)
                i = 0
            i_rand = random.randint(0, 2)
        print("Traffic light has wrong turn!")


my_traffic_light = TrafficLight()
my_traffic_light.running()
