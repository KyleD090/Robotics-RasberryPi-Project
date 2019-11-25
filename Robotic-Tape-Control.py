import time
from time import sleep
from di_sensors.light_color_sensor import LightColorSensor
from gopigo3 import *
import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()
lcs = LightColorSensor(led_state = True)

def turndegrees(degrees, speed):
    startpositionleft = gpg.get_motor_encoder(gpg.MOTOR_LEFT)
    startpositionright = gpg.get_motor_encoder(gpg.MOTOR_RIGHT)
    wheeltraveldistance = ((gpg.WHEEL_BASE_CIRCUMFERENCE * degrees) / 360)
    wheelturndegrees = ((wheeltraveldistance/gpg.WHEEL_CIRCUMFERENCE) * 360)
    gpg.set_motor_limits(gpg.MOTOR_LEFT + gpg.MOTOR_RIGHT, dps = speed)
    gpg.set_motor_position(gpg.MOTOR_LEFT, (startpositionleft + wheelturndegrees))
    gpg.set_motor_position(gpg.MOTOR_RIGHT, (startpositionleft - wheelturndegrees))


def follow_tape():
    value = 0
    while True:
        red, green, blue, clear = lcs.get_raw_colors()
        print("Red: {:5.3f} Green: {:5.3f} Blue: {:5.3f} Clear: {:5.3f}".format(red, green, blue, clear))
        time.sleep(0.02)
        if clear > 0.1:
            gpg.forward()
            value = 0
        elif value >= 0:
            value = value + 5
            value = value * -1
            turndegrees(value, 80)
            time.sleep(1.5)
            print("Value =" value)
        else:
            value = (value * -1) +5
            turndegrees(value, 80)
            time.sleep(1.5)
#follow_tape()
            
#To use numpad to direct to classroom 
Room_number = input(“What room do you want to go to?”)

def Go_to_room_number(Room_number): 
    if Room_number == 170:
        gpg.drive_cm(1040)
	gpg.stop()
def Return_home(Room_number):
    if Room_number == 170:
        gpg.right()
	time.sleep(2)
	gpg.stop()
	gpg.drive_cm(1040)
	gpg.stop()
	gpg.right()
	time.sleep(2)
	gpg.stop()

if Room_number == 170: 
	Go_to_room_number(170)
	Sleep(2)
	Return_home(170)

                           
                           
    
