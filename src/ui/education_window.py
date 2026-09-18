from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit
)


class EducationWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "MotoEléctric 3D - Módulo Educativo"
        )

        self.resize(900, 700)

        self.setup_ui()
        self.load_styles()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(15)

        title = QLabel(
            "Módulo Educativo"
        )

        title.setObjectName("title")

        subtitle = QLabel(
            "Motores eléctricos y cajas reductoras"
        )

        subtitle.setObjectName("subtitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2> Motores eléctricos</h2>

        <p>
        Un motor eléctrico es una máquina que transforma
        energía eléctrica en energía mecánica.
        </p>

        <h3>Principales variables</h3>

        <ul>
            <li><b>Voltaje:</b> tensión eléctrica aplicada al motor.</li>
            <li><b>Corriente:</b> cantidad de corriente consumida.</li>
            <li><b>Potencia:</b> capacidad de realizar trabajo.</li>
            <li><b>RPM:</b> revoluciones por minuto.</li>
            <li><b>Torque:</b> fuerza de giro producida por el motor.</li>
        </ul>

        <h2>⚙ Cajas reductoras</h2>

        <p>
        Una caja reductora utiliza engranajes para modificar
        la velocidad y el torque transmitido por el motor.
        </p>

        <h3>Relación de transmisión</h3>

        <p>
        La relación puede calcularse utilizando el número
        de dientes de los engranajes:
        </p>

        <p>
        <b>Relación = dientes de salida / dientes de entrada</b>
        </p>

        <h3>¿Qué ocurre al aumentar la relación?</h3>

        <p>
        Generalmente se reduce la velocidad de salida y
        aumenta el torque disponible, considerando las
        pérdidas de eficiencia del sistema.
        </p>

        <h2> Torque</h2>

        <p>
        El torque del motor puede calcularse mediante:
        </p>

        <p>
        <b>T = P / ω</b>
        </p>

        <p>
        donde P representa la potencia y ω la velocidad
        angular.
        </p>
        """)

        close_button = QPushButton(
            "Volver"
        )

        close_button.clicked.connect(
            self.close
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(content)
        layout.addWidget(close_button)

        central_widget.setLayout(layout)

    def load_styles(self):

        from pathlib import Path

        style_path = Path(__file__).parent / "styles" / "app.qss"

        with open(style_path, "r", encoding="utf-8") as file:
            self.setStyleSheet(file.read())