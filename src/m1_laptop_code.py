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

    #Grid Widgets
    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=2, column=0)
    distance_label.grid(row=1, column=3)
    distance_entry.grid(row=2, column=3)
    forward_button.grid(row=3, column=1)
    back_button.grid(row=3, column=2)

    #Set button callback
    forward_button['command'] = lambda: print("Forward button")
    back_button['command'] = lambda: print("Back button")
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
def go(mqtt_sender, direction,speed,distance):
    print()
    print("Robot is", direction)
    print("at a speed of:", speed)
    print("for a distance of:", distance)
    mqtt_sender.send_message("move", [speed, distance])

def move_forward(speed_entry_box,distance_entry_box, mqqt_sender):
    speed = int(speed_entry_box.get())
    dist = int(distance_entry_box.get())
    go(mqqt_sender,"MOVING FORWARD",speed,dist)

def move_backward(speed_entry_box,distance_entry_box, mqqt_sender):
    speed = -1*int(speed_entry_box.get())
    dist = int(distance_entry_box.get())
    move(mqqt_sender,"MOVING BACKWARD", speed, dist)
