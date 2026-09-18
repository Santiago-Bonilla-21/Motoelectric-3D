from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)


class MainMenu(QMainWindow):

    def __init__(self, username):
        super().__init__()

        self.username = username

        self.setWindowTitle("MotoEléctric 3D")
        self.setFixedSize(700, 600)

        self.setup_ui()
        self.load_styles()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setContentsMargins(60, 50, 60, 50)
        layout.setSpacing(20)

        title = QLabel("MOTOELÉCTRIC 3D")
        title.setObjectName("title")

        subtitle = QLabel(
            f"Bienvenido, {self.username}"
        )
        subtitle.setObjectName("subtitle")

        description = QLabel(
            "Seleccione el módulo que desea utilizar."
        )
        description.setObjectName("description")

        simulation_button = QPushButton(
            "⚙  SIMULAR MOTOR"
        )

        education_button = QPushButton(
            "📚  MÓDULO EDUCATIVO"
        )

        logout_button = QPushButton(
            "🚪  CERRAR SESIÓN"
        )

        simulation_button.clicked.connect(
            self.open_simulation
        )

        education_button.clicked.connect(
            self.open_education
        )

        logout_button.clicked.connect(
            self.logout
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(description)

        layout.addSpacing(30)

        layout.addWidget(simulation_button)
        layout.addWidget(education_button)

        layout.addStretch()

        layout.addWidget(logout_button)

        central_widget.setLayout(layout)

    def open_simulation(self):

        from src.ui.main_window import MainWindow

        self.simulation_window = MainWindow()
        self.simulation_window.show()

    def open_education(self):

        from src.ui.education_window import EducationWindow

        self.education_window = EducationWindow()
        self.education_window.show()

    def logout(self):

        from src.ui.login_window import LoginWindow

        self.login_window = LoginWindow()
        self.login_window.show()

        self.close()

    def load_styles(self):

        from pathlib import Path

        style_path = Path(__file__).parent / "styles" / "app.qss"

        with open(style_path, "r", encoding="utf-8") as file:
            self.setStyleSheet(file.read())