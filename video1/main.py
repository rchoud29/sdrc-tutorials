from gpiozero import Motor
import time

motor = Motor(enable=21, forward=20, backward=16)

motor.forward(1)

while True:
    time.sleep(1)

    motor.reverse()
