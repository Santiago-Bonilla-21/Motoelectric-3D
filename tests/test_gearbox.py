from src.models.gearbox import Gearbox


def test_gearbox_ratio():

    gearbox = Gearbox(
        input_teeth=20,
        output_teeth=60
    )

    assert gearbox.ratio() == 3