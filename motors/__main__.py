from gpiozero import Motor


if __name__ == "__main__":
    motor = Motor(20, 21)
    motor.forward()
    input("Press enter to stop")
    motor.stop()
    print("Stopped")
