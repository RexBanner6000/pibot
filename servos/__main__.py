from argparse import ArgumentParser
import time

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
    p = GPIO.PWM(5, 50)
    p.start(2.5)  # Initialization
    try:
        while True:
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
