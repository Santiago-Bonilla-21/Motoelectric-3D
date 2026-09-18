from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from src.database.database import authenticate_user


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MotoEléctric 3D - Iniciar sesión")
        self.setFixedSize(450, 500)

        self.setup_ui()
        self.load_styles()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(15)

        title = QLabel("MOTOELÉCTRIC 3D")
        title.setObjectName("title")

        subtitle = QLabel("Sistema de simulación y aprendizaje")
        subtitle.setObjectName("subtitle")

        username_label = QLabel("Usuario")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Ingrese su usuario")

        password_label = QLabel("Contraseña")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Ingrese su contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Iniciar sesión")
        login_button.clicked.connect(self.login)

        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.addSpacing(30)

        layout.addWidget(username_label)
        layout.addWidget(self.username_input)

        layout.addWidget(password_label)
        layout.addWidget(self.password_input)

        layout.addSpacing(20)

        layout.addWidget(login_button)

        layout.addStretch()

        central_widget.setLayout(layout)

    def login(self):

        username = self.username_input.text().strip()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(
                self,
                "Campos requeridos",
                "Ingrese usuario y contraseña."
            )
            return

        user = authenticate_user(username, password)

        if user:

            from src.ui.main_menu import MainMenu

            self.main_menu = MainMenu(username)
            self.main_menu.show()

            self.close()

        else:

            QMessageBox.warning(
                self,
                "Error de autenticación",
                "Usuario o contraseña incorrectos."
            )

    def load_styles(self):

        from pathlib import Path

        style_path = Path(__file__).parent / "styles" / "app.qss"

        with open(style_path, "r", encoding="utf-8") as file:
            self.setStyleSheet(file.read())