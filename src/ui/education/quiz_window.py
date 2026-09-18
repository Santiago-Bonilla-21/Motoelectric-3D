from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QButtonGroup,
    QMessageBox,
    QScrollArea,
    QGroupBox
)


class QuizWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "MotoEléctric 3D - Quiz"
        )

        self.resize(900, 700)

        self.questions = []
        self.groups = []

        self.setup_ui()
        self.load_styles()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            35, 30, 35, 30
        )

        main_layout.setSpacing(15)

        # ==========================================
        # ENCABEZADO
        # ==========================================

        header_layout = QHBoxLayout()

        title_layout = QVBoxLayout()

        title = QLabel("📝 QUIZ")
        title.setObjectName("title")

        subtitle = QLabel(
            "Comprueba tus conocimientos sobre motores "
            "eléctricos y cajas reductoras."
        )
        subtitle.setObjectName("subtitle")

        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)

        back_button = QPushButton("← Volver")
        back_button.setObjectName("backButton")
        back_button.clicked.connect(self.close)

        header_layout.addLayout(title_layout)
        header_layout.addStretch()
        header_layout.addWidget(back_button)

        main_layout.addLayout(header_layout)

        # ==========================================
        # ÁREA DE PREGUNTAS
        # ==========================================

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        questions_widget = QWidget()

        questions_layout = QVBoxLayout()
        questions_layout.setSpacing(20)

        self.add_question(
            questions_layout,
            1,
            "¿Qué transforma principalmente un motor eléctrico?",
            [
                "Energía mecánica en energía eléctrica",
                "Energía eléctrica en energía mecánica",
                "Energía térmica en energía eléctrica",
                "Energía química en energía mecánica"
            ],
            1
        )

        self.add_question(
            questions_layout,
            2,
            "¿Qué significa RPM?",
            [
                "Potencia real del motor",
                "Relación de potencia mecánica",
                "Revoluciones por minuto",
                "Resistencia por minuto"
            ],
            2
        )

        self.add_question(
            questions_layout,
            3,
            "¿Cuál es la unidad del torque?",
            [
                "Voltio",
                "Amperio",
                "Newton-metro",
                "Vatio"
            ],
            2
        )

        self.add_question(
            questions_layout,
            4,
            "¿Qué ocurre normalmente al utilizar una caja reductora?",
            [
                "Aumenta la velocidad y disminuye el torque",
                "Disminuye la velocidad y aumenta el torque",
                "Elimina completamente el torque",
                "Convierte RPM directamente en voltios"
            ],
            1
        )

        self.add_question(
            questions_layout,
            5,
            "Si la relación es 3:1 y el motor gira a 1800 RPM, "
            "¿cuál es la velocidad de salida?",
            [
                "600 RPM",
                "5400 RPM",
                "1803 RPM",
                "300 RPM"
            ],
            0
        )

        self.add_question(
            questions_layout,
            6,
            "¿Qué representa la eficiencia?",
            [
                "La cantidad de dientes del engranaje",
                "La velocidad máxima del motor",
                "La proporción de energía o potencia útil respecto a la entrada",
                "El número de revoluciones del eje"
            ],
            2
        )

        self.add_question(
            questions_layout,
            7,
            "¿Cuál es la fórmula simplificada para calcular "
            "potencia eléctrica?",
            [
                "P = V × I",
                "P = RPM / T",
                "P = T × V",
                "P = I / V"
            ],
            0
        )

        self.add_question(
            questions_layout,
            8,
            "Si un engranaje de entrada tiene 20 dientes y "
            "uno de salida tiene 60 dientes, ¿cuál es la relación?",
            [
                "0.33",
                "2",
                "3",
                "40"
            ],
            2
        )

        questions_layout.addSpacing(20)

        # ==========================================
        # BOTÓN COMPROBAR
        # ==========================================

        check_button = QPushButton(
            "✓ COMPROBAR RESPUESTAS"
        )

        check_button.clicked.connect(
            self.check_answers
        )

        questions_layout.addWidget(check_button)

        # ==========================================
        # RESULTADO
        # ==========================================

        self.result_label = QLabel("")
        self.result_label.setObjectName("sectionTitle")

        self.result_label.setWordWrap(True)

        questions_layout.addWidget(
            self.result_label
        )

        questions_layout.addStretch()

        questions_widget.setLayout(
            questions_layout
        )

        scroll.setWidget(
            questions_widget
        )

        main_layout.addWidget(scroll)

        central_widget.setLayout(
            main_layout
        )

    # ==========================================
    # CREAR PREGUNTA
    # ==========================================

    def add_question(
        self,
        layout,
        number,
        question,
        options,
        correct_answer
    ):

        group_box = QGroupBox(
            f"{number}. {question}"
        )

        question_layout = QVBoxLayout()

        button_group = QButtonGroup(
            self
        )

        radio_buttons = []

        for index, option in enumerate(options):

            radio = QRadioButton(
                option
            )

            button_group.addButton(
                radio,
                index
            )

            question_layout.addWidget(
                radio
            )

            radio_buttons.append(
                radio
            )

        group_box.setLayout(
            question_layout
        )

        layout.addWidget(
            group_box
        )

        self.groups.append(
            button_group
        )

        self.questions.append(
            {
                "correct": correct_answer,
                "group": button_group
            }
        )

    # ==========================================
    # COMPROBAR RESPUESTAS
    # ==========================================

    def check_answers(self):

        score = 0
        unanswered = 0

        for question in self.questions:

            selected = question[
                "group"
            ].checkedId()

            if selected == -1:

                unanswered += 1

            elif selected == question[
                "correct"
            ]:

                score += 1

        total = len(
            self.questions
        )

        if unanswered > 0:

            QMessageBox.warning(
                self,
                "Quiz incompleto",
                "Debes responder todas las preguntas."
            )

            return

        percentage = (
            score / total
        ) * 100

        if percentage >= 80:

            message = (
                "¡Excelente! Has demostrado un "
                "buen dominio de los conceptos."
            )

        elif percentage >= 60:

            message = (
                "¡Buen trabajo! Tienes una base "
                "adecuada, pero puedes seguir practicando."
            )

        else:

            message = (
                "Puedes seguir estudiando los módulos "
                "educativos y volver a intentarlo."
            )

        self.result_label.setText(
            f"Resultado: {score}/{total} "
            f"({percentage:.0f}%)\n\n"
            f"{message}"
        )

        QMessageBox.information(
            self,
            "Resultado del Quiz",
            f"Obtuviste {score} de {total} "
            f"respuestas correctas.\n\n"
            f"Calificación: {percentage:.0f}%"
        )

    # ==========================================
    # ESTILOS
    # ==========================================

    def load_styles(self):

        from pathlib import Path

        style_path = (
            Path(__file__).parent.parent
            / "styles"
            / "app.qss"
        )

        with open(
            style_path,
            "r",
            encoding="utf-8"
        ) as file:

            self.setStyleSheet(
                file.read()
            )