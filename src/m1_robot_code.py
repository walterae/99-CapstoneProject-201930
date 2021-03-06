"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Audrey Walters.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m2_robot_code as m2
import m3_robot_code as m3


class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def go(self, left_motor_speed, right_motor_speed):
        """ Tells the robot to go (i.e. move) using the given motor speeds. """
        print_message_received("go", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    # TODO: Add methods here as needed.
    def move(self,speed,distance):
        print_message_received("move",[speed,distance])
        self.robot.drive_system.go(speed,speed)
        self.robot.drive_system.left_motor.reset_position()
        wheel_dist = self.robot.drive_system.left_motor.get_position()*0.012
        while True:
            if wheel_dist > distance:
                break
            wheel_dist = self.robot.drive_system.left_motor.get_position()*0.012
        self.robot.drive_system.stop()

    def go_to(self,x,delta,speed):
        print_message_received("go_to",[x,delta,speed])
        self.robot.drive_system.go(speed,speed)
        dist_from=[]
        for k in range(5):
            dist_from = dist_from + [self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()]
            print(dist_from)
        while True:
            if (dist_from[1] + dist_from[2] + dist_from [3])/3 + delta < x or (dist_from[1] + dist_from[2] + dist_from [3])/3 - delta < x:
                break
            for k in range(4):
                dist_from[k] = dist_from[k+1]
            dist_from[4] = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            print(dist_from)
        self.robot.drive_system.stop()

        dist_from = []
        for k in range(5):
            dist_from = dist_from + [self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()]
            print(dist_from)

        if (dist_from[1] + dist_from[2] + dist_from[3]) / 3 + delta < x or (dist_from[1] + dist_from[2] + dist_from[3]) / 3 - delta < x:
            while True:
                if (dist_from[1] + dist_from[2] + dist_from[3]) / 3 + delta >= x or (dist_from[1] + dist_from[2] + dist_from[3]) / 3 - delta >= x:
                    break
                self.robot.drive_system.go(speed*(-0.25), speed*(-0.25))
            self.robot.drive_system.stop()

        else:
            while True:
                if (dist_from[1] + dist_from[2] + dist_from[3]) / 3 + delta < x or (
                        dist_from[1] + dist_from[2] + dist_from[3]) / 3 - delta < x:
                    break
                for k in range(4):
                    dist_from[k] = dist_from[k + 1]
                dist_from[4] = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
                print(dist_from)
            self.robot.drive_system.stop()


def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

