from gpiozero import Motor
from time import sleep


def cycle_motor(motor: Motor) -> None:
    for speed in [0.1, 0.5, 1]:
        motor.forward(speed=speed)
        sleep(1)
        motor.backward(speed=speed)
        sleep(1)
        motor.stop()


if __name__ == "__main__":

    front_right = Motor(20, 21)
    front_left = Motor(22, 23)
    back_left = Motor(24, 25)
    back_right = Motor(26, 27)

    for motor in [front_right, front_left, back_left, back_right]:
        cycle_motor(motor)
        motor.stop()
