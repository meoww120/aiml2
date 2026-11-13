import random

def get_sensor_data():
    temp = random.randint(20,60)
    light = bool(random.randint(0,1))
    motion = bool(random.randint(0,1))
    smoke = bool(random.randint(0,1))
    occup = bool(random.randint(0,1))

    return temp, motion, smoke, occup, light

def smart_home_agent():
    temp, motion, smoke, occup, light = get_sensor_data()

    if temp > 30 :
        print("temp over 30 --- *AC TURNED ON*\n")
    else:
        print("temp below 30 --- *AC TURNED OFF*\n")
    
    if motion and not light:
        print("motion and darkness detected --- *light TURNED ON*\n")
    elif motion and light:
        print("no darkness is detected --- *light TURNED OFF*\n")
    elif (not motion) and light:
        print("neither the motion nor the darkness is detected --- *light TURNED OFF*\n")
    else :
        print("darkness is detected --- *light TURNED on*\n")

    if smoke :
        print("smoke detected --- *FIRE ALARM TURNED ON*\n")
    else:
        print("smoke not detected --- *FIRE ALARM TURNED OFF*\n")

    if occup :
        print("room occupied --- *door unlocked*\n")
    else:
        print("room not occupied --- *door locked*\n")
    
smart_home_agent()