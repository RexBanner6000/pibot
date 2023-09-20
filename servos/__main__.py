import time
from argparse import ArgumentParser
from typing import Tuple

import RPi.GPIO as GPIO


class Servo:
    def __init__(
            self,
            pin: int,
            pulse_range: Tuple[float, float],
            rotation_range: Tuple[float, float],
            frequency: float = 50,
            dead_space: float = 0.05,
    ):
        self.pin = pin
        self.pulse_range = pulse_range
        self.rotation_range = rotation_range
        self.frequency = frequency
        self.dead_space = dead_space

    def initialise_pin(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def send_pulse(self, pulse_width: float) -> None:
        pulse = GPIO.PWM(self.pin, self.frequency)
        pulse.start(2.5)
        pulse.ChangeDutyCycle(pulse_width)
        time.sleep(self.dead_space)
        pulse.stop()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--pin", help="Pin number", type=int, default=5)
    parser.add_argument(
        "-d", "--duty_cycle", help="Duty cycle", type=float, default=5
    )

    args = parser.parse_args()

    servo = Servo(args.pin, (3.2, 11.2), (0, 180))
    servo.initialise_pin()
    servo.send_pulse(args.duty_cycle)

    GPIO.cleanup()
