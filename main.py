import sys

from PySide6.QtWidgets import QApplication

from src.database.database import (
    initialize_database,
    create_default_user
)

from src.ui.login_window import LoginWindow


def main():

    # Inicializar base de datos
    initialize_database()

    # Crear usuario inicial
    create_default_user()

    # Crear aplicación
    app = QApplication(sys.argv)

    # Mostrar login
    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()