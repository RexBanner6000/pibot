from argparse import ArgumentParser
from time import sleep

from gpiozero import Servo
from gpiozero.tools import sin_values
from signal import pause


class SweepingServo(Servo):
    def __init__(self, pin: int = 5):
        super(SweepingServo, self).__init__(pin)

    def sweep(self):
        self.source = sin_values()
        self.source_delay = 0.1

        pause()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--pin", help="Pin number", type=int, default=5)

    args = parser.parse_args()

    sweeping_servo = SweepingServo(args.pin)
    sweeping_servo.sweep()
