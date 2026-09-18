from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTabWidget,
    QTextEdit
)


class ConceptsWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "MotoEléctric 3D - Conceptos básicos"
        )

        self.resize(1000, 700)

        self.setup_ui()
        self.load_styles()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(35, 30, 35, 30)
        main_layout.setSpacing(15)

        # ==========================================
        # ENCABEZADO
        # ==========================================

        header_layout = QHBoxLayout()

        title_layout = QVBoxLayout()

        title = QLabel("CONCEPTOS BÁSICOS")
        title.setObjectName("title")

        subtitle = QLabel(
            "Aprende los conceptos fundamentales utilizados "
            "en la simulación de motores eléctricos."
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
        # PESTAÑAS
        # ==========================================

        tabs = QTabWidget()
        tabs.setObjectName("educationTabs")

        tabs.addTab(
            self.create_power_tab(),
            "Potencia"
        )

        tabs.addTab(
            self.create_torque_tab(),
            "Torque"
        )

        tabs.addTab(
            self.create_rpm_tab(),
            "RPM"
        )

        tabs.addTab(
            self.create_voltage_current_tab(),
            "V / A"
        )

        tabs.addTab(
            self.create_efficiency_tab(),
            "Eficiencia"
        )

        main_layout.addWidget(tabs)

        central_widget.setLayout(main_layout)

    # ==========================================
    # POTENCIA
    # ==========================================

    def create_power_tab(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("⚡ Potencia")
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>¿Qué es la potencia?</h2>

        <p>
        La <b>potencia</b> representa la cantidad de energía
        transferida o transformada por unidad de tiempo.
        </p>

        <p>
        En el Sistema Internacional se mide en
        <b>vatios (W)</b>.
        </p>

        <h3>Potencia eléctrica</h3>

        <p>
        Para un circuito eléctrico sencillo:
        </p>

        <p>
        <b>P = V × I</b>
        </p>

        <ul>
            <li>P = Potencia en vatios (W)</li>
            <li>V = Voltaje en voltios (V)</li>
            <li>I = Corriente en amperios (A)</li>
        </ul>

        <h3>Ejemplo</h3>

        <p>
        Si tenemos un motor de 220 V y consume 10 A:
        </p>

        <p>
        <b>P = 220 × 10 = 2200 W</b>
        </p>

        <p>
        Por lo tanto, la potencia eléctrica calculada es
        aproximadamente <b>2200 W</b>.
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # TORQUE
    # ==========================================

    def create_torque_tab(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Torque")
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>¿Qué es el torque?</h2>

        <p>
        El <b>torque</b>, también llamado momento de fuerza,
        representa la capacidad de una fuerza para producir
        rotación alrededor de un eje.
        </p>

        <p>
        Su unidad es el <b>Newton-metro (N·m)</b>.
        </p>

        <h3>Relación entre potencia, torque y velocidad</h3>

        <p>
        Para un sistema rotacional:
        </p>

        <p>
        <b>T = P / ω</b>
        </p>

        <ul>
            <li>T = Torque (N·m)</li>
            <li>P = Potencia (W)</li>
            <li>ω = Velocidad angular (rad/s)</li>
        </ul>

        <h3>Velocidad angular</h3>

        <p>
        La velocidad angular puede calcularse mediante:
        </p>

        <p>
        <b>ω = 2π × RPM / 60</b>
        </p>

        <h3>Ejemplo</h3>

        <p>
        Para un motor de 2200 W y 1800 RPM:
        </p>

        <p>
        ω = 2π × 1800 / 60
        </p>

        <p>
        ω ≈ 188.50 rad/s
        </p>

        <p>
        T = 2200 / 188.50
        </p>

        <p>
        <b>T ≈ 11.67 N·m</b>
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # RPM
    # ==========================================

    def create_rpm_tab(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("RPM")
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>¿Qué significa RPM?</h2>

        <p>
        <b>RPM</b> significa revoluciones por minuto.
        Es una unidad utilizada para expresar la velocidad
        de rotación de un eje.
        </p>

        <h3>Ejemplo</h3>

        <p>
        Si un motor trabaja a <b>1800 RPM</b>, significa que
        su eje realiza aproximadamente 1800 revoluciones
        completas cada minuto.
        </p>

        <h3>Conversión a velocidad angular</h3>

        <p>
        Para utilizar RPM en cálculos físicos se puede
        convertir a radianes por segundo:
        </p>

        <p>
        <b>ω = 2π × RPM / 60</b>
        </p>

        <h3>RPM en una caja reductora</h3>

        <p>
        Si una caja tiene una relación de reducción de 3:1:
        </p>

        <p>
        <b>RPM salida = RPM entrada / 3</b>
        </p>

        <p>
        Para 1800 RPM:
        </p>

        <p>
        <b>RPM salida = 600 RPM</b>
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # VOLTAJE Y CORRIENTE
    # ==========================================

    def create_voltage_current_tab(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("🔌 Voltaje y corriente")
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>Voltaje</h2>

        <p>
        El <b>voltaje</b> representa la diferencia de potencial
        eléctrico entre dos puntos.
        </p>

        <p>
        Se mide en <b>voltios (V)</b>.
        </p>

        <h2>Corriente</h2>

        <p>
        La <b>corriente eléctrica</b> representa el flujo de
        carga eléctrica a través de un conductor.
        </p>

        <p>
        Se mide en <b>amperios (A)</b>.
        </p>

        <h3>Relación con la potencia</h3>

        <p>
        En un modelo eléctrico sencillo:
        </p>

        <p>
        <b>P = V × I</b>
        </p>

        <h3>Ejemplo</h3>

        <p>
        Un motor recibe 220 V y consume 10 A:
        </p>

        <p>
        <b>P = 220 × 10 = 2200 W</b>
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # EFICIENCIA
    # ==========================================

    def create_efficiency_tab(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Eficiencia")
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>¿Qué es la eficiencia?</h2>

        <p>
        La <b>eficiencia</b> indica qué proporción de la energía
        o potencia de entrada se convierte en energía o potencia
        útil de salida.
        </p>

        <p>
        Normalmente se expresa como porcentaje.
        </p>

        <h3>Fórmula</h3>

        <p>
        <b>η = (Potencia de salida / Potencia de entrada) × 100</b>
        </p>

        <h3>Ejemplo</h3>

        <p>
        Si un sistema recibe 1000 W y entrega 900 W:
        </p>

        <p>
        <b>η = (900 / 1000) × 100 = 90%</b>
        </p>

        <h3>En una caja reductora</h3>

        <p>
        La eficiencia permite representar las pérdidas que
        existen durante la transmisión debido, entre otros
        factores, a la fricción y otras pérdidas mecánicas.
        </p>

        <p>
        Por ejemplo, una caja reductora con una eficiencia
        del <b>90%</b> transmite aproximadamente el 90% de
        la potencia disponible, bajo el modelo simplificado
        utilizado por el simulador.
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

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

            self.setStyleSheet(file.read())