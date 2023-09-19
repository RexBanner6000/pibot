import time

import RPi.GPIO as GPIO


def init(servo_pin: int = 5) -> None:
    GPIO.setup(servo_pin, GPIO.OUT)


def servo_pulse(servo_pin: int = 5, angle: float = 5) -> None:
    pulse_width = angle * 11 + 500
    GPIO.output(servo_pin, GPIO.HIGH)
    time.sleep(pulse_width / 1_000_000.0)
    GPIO.output(servo_pin, GPIO.LOW)
    time.sleep(20e-3 - pulse_width / 1_000_000.0)


if __name__ == "__main__":
    rotation = 5
    init(servo_pin=5)
    print(f"Rotating servo {rotation}")
    servo_pulse()
    print("Done!")
