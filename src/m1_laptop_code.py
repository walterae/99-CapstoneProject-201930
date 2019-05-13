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

def main():
    print()

def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Audrey Walters")
    frame_label.grid()
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    # root.title("MQTT Remote")
    #
    # main_frame = ttk.Frame(root, padding=20)
    # main_frame.grid()  # only grid call that does NOT need a row and column
    #
    # left_speed_label = ttk.Label(main_frame, text="Left")
    # left_speed_label.grid(row=0, column=0)
    # left_speed_entry = ttk.Entry(main_frame, width=8)
    # left_speed_entry.insert(0, "600")
    # left_speed_entry.grid(row=1, column=0)
    #
    # right_speed_label = ttk.Label(main_frame, text="Right")
    # right_speed_label.grid(row=0, column=2)
    # right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    # right_speed_entry.insert(0, "600")
    # right_speed_entry.grid(row=1, column=2)
    #
    # forward_button = ttk.Button(main_frame, text="Forward")
    # forward_button.grid(row=2, column=1)
    # forward_button['command'] = lambda: print("Forward button")
    # root.bind('<Up>', lambda event: print("Forward key"))
    #
    # left_button = ttk.Button(main_frame, text="Left")
    # left_button.grid(row=3, column=0)
    # left_button['command'] = lambda: print("Left button")
    # root.bind('<Left>', lambda event: print("Left key"))
    #
    # stop_button = ttk.Button(main_frame, text="Stop")
    # stop_button.grid(row=3, column=1)
    # stop_button['command'] = lambda: print("Stop button")
    # root.bind('<space>', lambda event: print("Stop key"))
    #
    # right_button = ttk.Button(main_frame, text="Right")
    # right_button.grid(row=3, column=2)
    # right_button['command'] = lambda: print("Right button")
    # root.bind('<Right>', lambda event: print("Right key"))
    #
    # back_button = ttk.Button(main_frame, text="Back")
    # back_button.grid(row=4, column=1)
    # back_button['command'] = lambda: print("Back button")
    # root.bind('<Down>', lambda event: print("Back key"))
    #
    # up_button = ttk.Button(main_frame, text="Up")
    # up_button.grid(row=5, column=0)
    # up_button['command'] = lambda: print("Up button")
    # root.bind('<u>', lambda event: print("Up key"))
    #
    # down_button = ttk.Button(main_frame, text="Down")
    # down_button.grid(row=6, column=0)
    # down_button['command'] = lambda: print("Down button")
    # root.bind('<j>', lambda event: print("Down key"))
    #
    # # Buttons for quit and exit
    # q_button = ttk.Button(main_frame, text="Quit")
    # q_button.grid(row=5, column=2)
    # q_button['command'] = lambda: print("Quit button")
    #
    # e_button = ttk.Button(main_frame, text="Exit")
    # e_button.grid(row=6, column=2)
    # e_button['command'] = lambda: exit()
    #
    # root.mainloop()

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

def forward(speed,distance, mqqt_sender):
    print()

main()