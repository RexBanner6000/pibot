import time
from argparse import ArgumentParser

import RPi.GPIO as GPIO


def init(servo_pin: int = 5) -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)


def servo_pulse(servo_pin: int = 5, angle: float = 5) -> None:
    pulse_width = angle * 11 + 500
    GPIO.output(servo_pin, GPIO.HIGH)
    time.sleep(pulse_width / 1_000_000.0)
    GPIO.output(servo_pin, GPIO.LOW)
    time.sleep(20e-3 - pulse_width / 1_000_000.0)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--pin", help="Pin number", type=int, default=5)
    parser.add_argument(
        "-d", "--duty_cycle", help="Duty cycle", type=float, default=5
    )

    args = parser.parse_args()

    init(args.pin)
    p = GPIO.PWM(args.pin, 50)
    p.start(2.5)  # Initialization

    p.ChangeDutyCycle(args.duty_cycle)
    time.sleep(0.5)

    p.stop()
    GPIO.cleanup()
