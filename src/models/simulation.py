class Simulation:

    def __init__(self, motor, gearbox):
        self.motor = motor
        self.gearbox = gearbox

    def run(self):

        input_rpm = self.motor.rpm
        input_torque = self.motor.torque()

        ratio = self.gearbox.ratio()

        output_rpm = self.gearbox.output_rpm(input_rpm)

        output_torque = self.gearbox.output_torque(input_torque)

        return {
            "input_rpm": input_rpm,
            "input_torque": input_torque,
            "ratio": ratio,
            "output_rpm": output_rpm,
            "output_torque": output_torque,
            "efficiency": self.gearbox.efficiency
        }