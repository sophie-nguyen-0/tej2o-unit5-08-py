"""
Created by: sophie
Created on: dec 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *


distance_to_object = number = 0

# setup
display.show(Image.HEART)

while True:
    if (button_a.is_pressed() === true):
        display.clear
        while True:
            # Distance from sonar

            distance_to_object = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)

            if distance_to_object < 10:
                robotbit.stp_car_move(-10, 48)
                sleep(500)
                robotbit.stepper_turn(robotbit.Steppers.M1, robotbit.Turns.T1B4)
                sleep(500)
                robotbit.stepper_turn(robotbit.Steppers.M2, robotbit.Turns.T1B4)
                sleep(500)
                robotbit.stp_car_move(10, 48)
            else:
                # move forward
                robotbit.stp_car_move(10, 48)