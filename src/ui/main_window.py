from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MotoEléctric 3D")
        self.resize(1000, 700)

        title = QLabel("MotoEléctric 3D")

        subtitle = QLabel(
            "Simulador de motores eléctricos y cajas reductoras"
        )

        button = QPushButton("Ejecutar simulación")

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)