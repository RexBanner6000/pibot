from argparse import ArgumentParser
from time import sleep

from gpiozero import Servo


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--pin", help="Pin number", type=int, default=5)

    args = parser.parse_args()

    servo = Servo(args.pin)
    servo.min()
    sleep(2)
    servo.mid()
    sleep(2)
    servo.max()
    sleep(2)
