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


class ExamplesWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "MotoEléctric 3D - Ejemplos prácticos"
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

        title = QLabel("🧪 EJEMPLOS PRÁCTICOS")
        title.setObjectName("title")

        subtitle = QLabel(
            "Aplica los conceptos de motores y cajas reductoras "
            "mediante ejercicios prácticos."
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
            self.create_example_power(),
            "⚡ Potencia"
        )

        tabs.addTab(
            self.create_example_torque(),
            "💪 Torque"
        )

        tabs.addTab(
            self.create_example_gearbox(),
            "⚙ Reducción"
        )

        tabs.addTab(
            self.create_example_efficiency(),
            "📈 Eficiencia"
        )

        tabs.addTab(
            self.create_complete_example(),
            "🚀 Caso completo"
        )

        main_layout.addWidget(tabs)

        central_widget.setLayout(main_layout)

    # ==========================================
    # EJEMPLO 1 - POTENCIA
    # ==========================================

    def create_example_power(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel(
            "Ejemplo 1: cálculo de potencia"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>⚡ Calcular potencia eléctrica</h2>

        <p>
        Supongamos que tenemos un motor conectado a:
        </p>

        <ul>
            <li>Voltaje = 220 V</li>
            <li>Corriente = 10 A</li>
        </ul>

        <h3>Fórmula</h3>

        <p>
        <b>P = V × I</b>
        </p>

        <h3>Cálculo</h3>

        <p>
        P = 220 × 10
        </p>

        <p>
        <b>P = 2200 W</b>
        </p>

        <h3>Resultado</h3>

        <p>
        El motor presenta una potencia eléctrica calculada
        de aproximadamente <b>2200 W</b> bajo este modelo
        simplificado.
        """)
        
        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # EJEMPLO 2 - TORQUE
    # ==========================================

    def create_example_torque(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel(
            "Ejemplo 2: cálculo de torque"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>💪 Calcular torque del motor</h2>

        <p>
        Datos:
        </p>

        <ul>
            <li>Potencia = 2200 W</li>
            <li>Velocidad = 1800 RPM</li>
        </ul>

        <h3>Paso 1: convertir RPM</h3>

        <p>
        <b>ω = 2π × RPM / 60</b>
        </p>

        <p>
        ω = 2π × 1800 / 60
        </p>

        <p>
        ω ≈ 188.50 rad/s
        </p>

        <h3>Paso 2: calcular torque</h3>

        <p>
        <b>T = P / ω</b>
        </p>

        <p>
        T = 2200 / 188.50
        </p>

        <p>
        <b>T ≈ 11.67 N·m</b>
        </p>

        <h3>Resultado</h3>

        <p>
        El torque aproximado del motor es
        <b>11.67 N·m</b>.
        """)
        
        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # EJEMPLO 3 - CAJA REDUCTORA
    # ==========================================

    def create_example_gearbox(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel(
            "Ejemplo 3: caja reductora"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>⚙ Calcular la salida de una caja reductora</h2>

        <p>
        Datos:
        </p>

        <ul>
            <li>RPM de entrada = 1800 RPM</li>
            <li>Dientes de entrada = 20</li>
            <li>Dientes de salida = 60</li>
        </ul>

        <h3>Paso 1: relación de transmisión</h3>

        <p>
        <b>Relación = dientes de salida / dientes de entrada</b>
        </p>

        <p>
        Relación = 60 / 20
        </p>

        <p>
        <b>Relación = 3</b>
        </p>

        <h3>Paso 2: RPM de salida</h3>

        <p>
        <b>RPM salida = RPM entrada / relación</b>
        </p>

        <p>
        RPM salida = 1800 / 3
        </p>

        <p>
        <b>RPM salida = 600 RPM</b>
        </p>

        <h3>Resultado</h3>

        <p>
        La caja reductora disminuye la velocidad de
        <b>1800 RPM a 600 RPM</b>.
        """)
        
        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # EJEMPLO 4 - EFICIENCIA
    # ==========================================

    def create_example_efficiency(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel(
            "Ejemplo 4: eficiencia"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>📈 Aplicar eficiencia a la transmisión</h2>

        <p>
        Supongamos que:
        </p>

        <ul>
            <li>Torque de entrada = 11.67 N·m</li>
            <li>Relación = 3</li>
            <li>Eficiencia = 90%</li>
        </ul>

        <h3>Fórmula simplificada</h3>

        <p>
        <b>T salida = T entrada × relación × eficiencia</b>
        </p>

        <h3>Cálculo</h3>

        <p>
        T salida = 11.67 × 3 × 0.90
        </p>

        <p>
        <b>T salida ≈ 31.51 N·m</b>
        </p>

        <h3>Resultado</h3>

        <p>
        El torque de salida aproximado es
        <b>31.51 N·m</b>.
        </p>

        <p>
        La eficiencia del 90% representa las pérdidas
        consideradas en el modelo simplificado.
        """)
        
        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # CASO COMPLETO
    # ==========================================

    def create_complete_example(self):

        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel(
            "Ejemplo completo de simulación"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>🚀 Simulación completa</h2>

        <h3>Datos del motor</h3>

        <ul>
            <li>Potencia: 2200 W</li>
            <li>Voltaje: 220 V</li>
            <li>Corriente: 10 A</li>
            <li>RPM: 1800</li>
        </ul>

        <h3>Datos de la caja reductora</h3>

        <ul>
            <li>Dientes de entrada: 20</li>
            <li>Dientes de salida: 60</li>
            <li>Eficiencia: 90%</li>
        </ul>

        <h3>Resultados</h3>

        <table border="1" cellpadding="8">
            <tr>
                <th>Variable</th>
                <th>Resultado</th>
            </tr>

            <tr>
                <td>Torque de entrada</td>
                <td>≈ 11.67 N·m</td>
            </tr>

            <tr>
                <td>Relación</td>
                <td>3:1</td>
            </tr>

            <tr>
                <td>RPM de salida</td>
                <td>600 RPM</td>
            </tr>

            <tr>
                <td>Torque de salida</td>
                <td>≈ 31.51 N·m</td>
            </tr>

            <tr>
                <td>Eficiencia</td>
                <td>90%</td>
            </tr>
        </table>

        <h3>Interpretación</h3>

        <p>
        El sistema utiliza una caja reductora 3:1 para disminuir
        la velocidad del motor y aumentar el torque disponible
        en el eje de salida, considerando una eficiencia del 90%.
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