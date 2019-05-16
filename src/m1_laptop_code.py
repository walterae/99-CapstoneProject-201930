"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Audrey Walters.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3

def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Audrey Walters")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    # Consruct widgets

    speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, "50")
    distance_label = ttk.Label(frame, text="Distance (0 to 100)")
    distance_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    distance_entry.insert(0, "50")
    forward_button = ttk.Button(frame, text="Forwards")
    back_button = ttk.Button(frame, text="Backwards")
    delta_label =ttk.Label(frame,text="Delta")
    delta_entry = ttk.Entry(frame, width=8)
    delta_entry.insert(0,"1")
    go_until_button = ttk.Button(frame, text ="Go Until")
    x_label = ttk.Label(frame, text ="X")
    x_entry = ttk.Entry(frame, width =8)
    x_entry.insert(0,"5")
    plus_or_minus_label = ttk.Label(frame, text="+ or -")

    #Grid Widgets
    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=2, column=0)
    distance_label.grid(row=1, column=5)
    distance_entry.grid(row=2, column=5)
    forward_button.grid(row=4, column=2)
    back_button.grid(row=4, column=4)
    delta_label.grid(row=1, column =4)
    delta_entry.grid(row=2, column=4)
    go_until_button.grid(row=3, column=3)
    x_label.grid(row=1, column=2)
    x_entry.grid(row=2, column=2)
    plus_or_minus_label.grid(row=1, column=3)

    #Set button callback
    forward_button['command'] = lambda:(move_forward(speed_entry,distance_entry,mqtt_sender))
    back_button['command'] = lambda:(move_backward(speed_entry,distance_entry,mqtt_sender))
    go_until_button['command'] = lambda:(go_until_distance(x_entry,delta_entry,speed_entry,mqtt_sender))
    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.

# TODO: Add functions here as needed.
def move(mqtt_sender, direction,speed,distance):
    print()
    print("Robot is", direction)
    print("at a speed of:", speed)
    print("for a distance of: {} inches".format(distance))
    mqtt_sender.send_message("move", [speed, distance])

def go_to(mqqt_sender,function,x,delta,speed):
    print()
    print("Robot is",function)
    print("it is {} inches +/- {} inches away from nearest object".format(x,delta))
    print("at a speed of:",speed)
    mqqt_sender.send_message("go_to", [x, delta, speed])

def move_forward(speed_entry_box,distance_entry_box, mqqt_sender):
    speed = int(speed_entry_box.get())
    dist = int(distance_entry_box.get())
    move(mqqt_sender,"MOVING FORWARD",speed,dist)

def move_backward(speed_entry_box,distance_entry_box, mqqt_sender):
    speed = -1*int(speed_entry_box.get())
    dist = int(distance_entry_box.get())
    move(mqqt_sender,"MOVING BACKWARD", speed, dist)

def go_until_distance(x,delta,speed,mqqt_sender):
    x = int(x.get())
    delta = int(delta.get())
    speed = int(speed.get())
    go_to(mqqt_sender,"GOING UNTIL", x, delta, speed)
