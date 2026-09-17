from src.models.motor import Motor


def test_motor_torque():

    motor = Motor(
        voltage=220,
        current=10,
        rpm=1800,
        power=2200
    )

    torque = motor.torque()

    assert torque > 0