class Gearbox:
    def __init__(self, input_teeth, output_teeth, efficiency=0.90):
        self.input_teeth = input_teeth
        self.output_teeth = output_teeth
        self.efficiency = efficiency

    def ratio(self):
        if self.input_teeth == 0:
            return 0

        return self.output_teeth / self.input_teeth

    def output_rpm(self, input_rpm):
        ratio = self.ratio()

        if ratio == 0:
            return 0

        return input_rpm / ratio

    def output_torque(self, input_torque):
        return input_torque * self.ratio() * self.efficiency