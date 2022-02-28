#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
B = Motor(Port.B)
C = Motor(Port.C)
touch = TouchSensor(Port.S1)

loop1 = 1
loop2 = 1

while loop1 <= 2: 
    B.run_angle(300,360,Stop.BRAKE,False)
    C.run_angle(300,360,Stop.BRAKE,True)

    B.run_angle(100,360,Stop.BRAKE,True)

    loop1 = loop1 + 1
    

while loop2 <= 2:
    B.run_angle(300,360,Stop.BRAKE,False)
    C.run_angle(300,360,Stop.BRAKE,True)

    C.run_angle(100,360,Stop.BRAKE,True)

    loop2 = loop2 + 1
 

B.run_angle(300,360,Stop.BRAKE,False)
C.run_angle(300,360,Stop.BRAKE,True)












# Write your program here.
ev3.speaker.beep()
