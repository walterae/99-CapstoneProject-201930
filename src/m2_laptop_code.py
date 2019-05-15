"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Tyrique Jackson
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Tyrique Jackson")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    speed_label = ttk.Label(frame, text='Speed (0 to 100)')
    speed_entry = ttk.Entry(frame, width=8)
    left_length_label = ttk.Label(frame, text='left length (0 to 60)')
    left_length_entry = ttk.Entry(frame, width=8)
    right_length_label = ttk.Label(frame, text='right length (0 to 60)')
    right_length_entry = ttk.Entry(frame, width=8)
    left_spin_button = ttk.Button(frame, text='Spin Left')
    right_spin_button = ttk.Button(frame, text='Spin Right')

    # Grid Widgets
    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=2, column=0)
    left_length_label.grid(row=1, column=2)
    left_length_entry.grid(row=2, column=2)
    right_length_label.grid(row=1, column=3)
    right_length_entry.grid(row=2, column=3)
    left_spin_button.grid(row=3, column=1)
    right_spin_button.grid(row=3, column=2)

    # Set button callback
    left_spin_button['command'] = lambda: (spin_left(left_length_entry, speed_entry, mqtt_sender))
    right_spin_button['command'] = lambda: (spin_right(right_length_entry, speed_entry, mqtt_sender))


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
        self.mqtt_sender = mqtt_sende

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.

def spin(mqtt_sender, left_length, right_length, speed):
    print()
    print('For a speed of', speed)
    print('For a left length of', left_length)
    print('For a right length of', right_length)
    mqtt_sender.send_message("spin", [left_length, right_length])


def spin_left(left_length_entry_box, speed_entry_box, mqqt_sender):
    speed = int(speed_entry_box.get())
    left_length = int(left_length_entry_box.get())
    spin(mqqt_sender, 'Spinning Left', left_length, speed)


def spin_right(right_length_entry_box, speed_entry_box, mqqt_sender):
    speed = int(speed_entry_box.get())
    right_length = int(right_length_entry_box.get())
    spin(mqqt_sender, 'Spinning Right', right_length, speed)
