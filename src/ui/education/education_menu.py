from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton
)


class EducationMenu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MotoEléctric 3D - Educación")
        self.resize(900, 700)

        self.setup_ui()
        self.load_styles()

    def setup_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 40, 50, 40)
        main_layout.setSpacing(20)

        # Título
        title = QLabel("MÓDULO EDUCATIVO")
        title.setObjectName("title")

        subtitle = QLabel(
            "Aprende los fundamentos de los motores "
            "eléctricos y las cajas reductoras"
        )

        subtitle.setObjectName("subtitle")

        # Grid de tarjetas
        grid = QGridLayout()
        grid.setSpacing(20)

        # Motores
        motor_button = QPushButton(
            "\n\nMOTORES ELÉCTRICOS\n\n"
            "Funcionamiento y componentes"
        )

        motor_button.setObjectName("educationCard")
        motor_button.clicked.connect(self.open_motors)

        # Cajas
        gearbox_button = QPushButton(
            "\n\nCAJAS REDUCTORAS\n\n"
            "Engranajes y transmisión"
        )

        gearbox_button.setObjectName("educationCard")
        gearbox_button.clicked.connect(self.open_gearboxes)

        # Conceptos
        concepts_button = QPushButton(
            "\n\nCONCEPTOS BÁSICOS\n\n"
            "RPM, torque, potencia y eficiencia"
        )

        concepts_button.setObjectName("educationCard")
        concepts_button.clicked.connect(self.open_concepts)

        # Ejemplos
        examples_button = QPushButton(
            "\n\nEJEMPLOS PRÁCTICOS\n\n"
            "Aprende mediante ejercicios"
        )

        examples_button.setObjectName("educationCard")
        examples_button.clicked.connect(self.open_examples)

        # Quiz
        quiz_button = QPushButton(
            "\n\nQUIZ\n\n"
            "Comprueba tus conocimientos"
        )

        quiz_button.setObjectName("educationCard")
        quiz_button.clicked.connect(self.open_quiz)

        grid.addWidget(motor_button, 0, 0)
        grid.addWidget(gearbox_button, 0, 1)
        grid.addWidget(concepts_button, 1, 0)
        grid.addWidget(examples_button, 1, 1)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)
        main_layout.addSpacing(20)
        main_layout.addLayout(grid)
        main_layout.addWidget(quiz_button)

        back_button = QPushButton("← Volver al menú principal")
        back_button.setObjectName("backButton")
        back_button.clicked.connect(self.close)

        main_layout.addWidget(back_button)

        central.setLayout(main_layout)

    def open_motors(self):

        from src.ui.education.motors_window import MotorsWindow

        self.motors_window = MotorsWindow()
        self.motors_window.show()

    def open_gearboxes(self):

        from src.ui.education.gearboxes_window import GearboxesWindow

        self.gearboxes_window = GearboxesWindow()
        self.gearboxes_window.show()

    def open_concepts(self):

        from src.ui.education.concepts_window import ConceptsWindow

        self.concepts_window = ConceptsWindow()
        self.concepts_window.show()

    def open_examples(self):

        from src.ui.education.examples_window import ExamplesWindow

        self.examples_window = ExamplesWindow()
        self.examples_window.show()

    def open_quiz(self):

        from src.ui.education.quiz_window import QuizWindow

        self.quiz_window = QuizWindow()
        self.quiz_window.show()

    def load_styles(self):

        from pathlib import Path

        style_path = (
            Path(__file__).parent.parent
            / "styles"
            / "app.qss"
        )

        with open(style_path, "r", encoding="utf-8") as file:
            self.setStyleSheet(file.read())