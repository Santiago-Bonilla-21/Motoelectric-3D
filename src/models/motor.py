import math


class Motor:
    def __init__(self, voltage, current, rpm, power):
        self.voltage = voltage
        self.current = current
        self.rpm = rpm
        self.power = power

    def angular_velocity(self):
        return 2 * math.pi * self.rpm / 60

    def torque(self):
        omega = self.angular_velocity()

        if omega == 0:
            return 0

        return self.power / omega