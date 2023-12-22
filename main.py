"""
Created by: sophie
Created on: dec 2023
This module is a Micro:bit MicroPython program
"""

import robotbit
import sonar

# setup
basic.show_icon(IconNames.GHOST)

# loop forever
while True:
    if input.button_is_pressed(Button.A):
        while True:
            # check distance
            distance_to_object = sonar.ping(
                DigitalPin.P1,
                DigitalPin.P2,
                PingUnit.CENTIMETERS
            )
            basic.show_number(distance_to_object)

            # if distance is >= 10 motors move 10 cm forward
            if distance_to_object >= 10:
                robotbit.stp_car_move(10, 42)
                basic.pause(500)

            # if stepper motor is < 10 cm motors move 10 cm backward & turn 90 deegres
            else:
                robotbit.stp_car_move(-10, 42)
                basic.pause(500)
                robotbit.stp_car_turn(90, 42, 125)
                basic.pause(500)
                