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


class GearboxesWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "MotoEléctric 3D - Cajas reductoras"
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

        title = QLabel("⚙ CAJAS REDUCTORAS")
        title.setObjectName("title")

        subtitle = QLabel(
            "Conoce los engranajes, relaciones de transmisión "
            "y funcionamiento de las cajas reductoras."
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
            self.create_introduction_tab(),
            "📖 Introducción"
        )

        tabs.addTab(
            self.create_components_tab(),
            "⚙ Componentes"
        )

        tabs.addTab(
            self.create_operation_tab(),
            "🔄 Funcionamiento"
        )

        tabs.addTab(
            self.create_ratio_tab(),
            "📐 Relación"
        )

        tabs.addTab(
            self.create_variables_tab(),
            "📊 Variables"
        )

        main_layout.addWidget(tabs)

        central_widget.setLayout(main_layout)

    # ==========================================
    # 1. INTRODUCCIÓN
    # ==========================================

    def create_introduction_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)

        title = QLabel(
            "¿Qué es una caja reductora?"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>⚙ Caja reductora</h2>

        <p>
        Una <b>caja reductora</b> es un sistema mecánico
        compuesto principalmente por engranajes que permite
        modificar la velocidad de rotación y el torque
        transmitido desde un motor hacia una carga.
        </p>

        <p>
        En muchas aplicaciones, el motor gira a una velocidad
        demasiado alta para mover directamente una carga.
        La caja reductora permite disminuir la velocidad de
        salida y aumentar el torque disponible.
        </p>

        <h3>¿Para qué sirve?</h3>

        <ul>
            <li>Reducir la velocidad de giro.</li>
            <li>Aumentar el torque disponible.</li>
            <li>Transmitir movimiento entre ejes.</li>
            <li>Adaptar el motor a diferentes cargas.</li>
            <li>Controlar las características del movimiento.</li>
        </ul>

        <h3>Aplicaciones</h3>

        <ul>
            <li>Vehículos eléctricos.</li>
            <li>Robótica.</li>
            <li>Maquinaria industrial.</li>
            <li>Bandas transportadoras.</li>
            <li>Sistemas de automatización.</li>
            <li>Máquinas y mecanismos mecánicos.</li>
        </ul>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # 2. COMPONENTES
    # ==========================================

    def create_components_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(10)

        title = QLabel(
            "Componentes principales"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>🔩 Elementos de una caja reductora</h2>

        <p>
        Una caja reductora está formada por diferentes
        componentes que trabajan conjuntamente para transmitir
        el movimiento del motor hacia la carga.
        </p>

        <h3>⚙ Engranaje de entrada</h3>

        <p>
        Es el engranaje conectado al eje del motor.
        Recibe el movimiento y la potencia de entrada.
        </p>

        <h3>⚙ Engranaje de salida</h3>

        <p>
        Es el engranaje que transmite el movimiento hacia
        la carga. Su tamaño y número de dientes influyen
        directamente en la relación de transmisión.
        </p>

        <h3>🔄 Ejes</h3>

        <p>
        Los ejes soportan los engranajes y permiten transmitir
        el movimiento de rotación entre los diferentes
        componentes.
        </p>

        <h3>🛢 Lubricación</h3>

        <p>
        El lubricante reduce la fricción y el desgaste entre
        las superficies de los engranajes.
        </p>

        <h3>🛡 Carcasa</h3>

        <p>
        Protege los componentes internos y mantiene los
        elementos correctamente posicionados.
        </p>

        <h3>🔩 Rodamientos</h3>

        <p>
        Permiten que los ejes giren con menor fricción y
        ayudan a soportar las cargas mecánicas.
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # 3. FUNCIONAMIENTO
    # ==========================================

    def create_operation_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(10)

        title = QLabel(
            "¿Cómo funciona una caja reductora?"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>🔄 Principio de funcionamiento</h2>

        <p>
        El funcionamiento de una caja reductora se basa en
        la transmisión de movimiento mediante engranajes.
        </p>

        <h3>1. Entrada del movimiento</h3>

        <p>
        El motor proporciona una velocidad de rotación y un
        torque al eje de entrada de la caja reductora.
        </p>

        <h3>2. Transmisión mediante engranajes</h3>

        <p>
        El engranaje de entrada transmite su movimiento hacia
        uno o varios engranajes conectados.
        </p>

        <h3>3. Reducción de velocidad</h3>

        <p>
        Cuando el engranaje de salida tiene más dientes que
        el engranaje de entrada, la velocidad de salida
        disminuye.
        </p>

        <h3>4. Aumento del torque</h3>

        <p>
        Al reducir la velocidad, se obtiene un mayor torque
        disponible en el eje de salida, considerando las
        pérdidas de eficiencia del sistema.
        </p>

        <h3>5. Movimiento de la carga</h3>

        <p>
        Finalmente, el eje de salida transmite el movimiento
        hacia la carga mecánica.
        </p>

        <h3>Ejemplo</h3>

        <p>
        Si un motor gira a <b>1800 RPM</b> y se utiliza una
        relación de reducción de <b>3:1</b>, la velocidad de
        salida ideal será aproximadamente:
        </p>

        <p>
        <b>1800 / 3 = 600 RPM</b>
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # 4. RELACIÓN DE TRANSMISIÓN
    # ==========================================

    def create_ratio_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(10)

        title = QLabel(
            "Relación de transmisión"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>📐 Relación de transmisión</h2>

        <p>
        La relación de transmisión permite determinar cómo
        cambia la velocidad entre el eje de entrada y el eje
        de salida.
        </p>

        <h3>Fórmula</h3>

        <p>
        <b>Relación = Dientes de salida / Dientes de entrada</b>
        </p>

        <h3>Ejemplo</h3>

        <p>
        Supongamos que tenemos:
        </p>

        <ul>
            <li>Engranaje de entrada: 20 dientes</li>
            <li>Engranaje de salida: 60 dientes</li>
        </ul>

        <p>
        Entonces:
        </p>

        <p>
        <b>Relación = 60 / 20 = 3</b>
        </p>

        <p>
        Esto significa que tenemos una relación de reducción
        de <b>3:1</b>.
        </p>

        <h3>Velocidad de salida</h3>

        <p>
        La velocidad de salida puede calcularse mediante:
        </p>

        <p>
        <b>RPM salida = RPM entrada / Relación</b>
        </p>

        <p>
        Si el motor gira a 1800 RPM:
        </p>

        <p>
        <b>RPM salida = 1800 / 3 = 600 RPM</b>
        </p>

        <h3>Torque</h3>

        <p>
        En una caja reductora ideal, una mayor relación de
        reducción permite obtener un mayor torque de salida.
        En un sistema real se deben considerar las pérdidas
        de eficiencia.
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # 5. VARIABLES
    # ==========================================

    def create_variables_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(10)

        title = QLabel(
            "Variables importantes"
        )
        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>📊 Variables utilizadas en la simulación</h2>

        <h3>⚙ Número de dientes</h3>

        <p>
        Representa la cantidad de dientes presentes en cada
        engranaje. Influye directamente en la relación de
        transmisión.
        </p>

        <h3>🔄 RPM de entrada</h3>

        <p>
        Representa la velocidad de rotación proporcionada por
        el motor al sistema de transmisión.
        </p>

        <h3>🔄 RPM de salida</h3>

        <p>
        Representa la velocidad de rotación disponible después
        de pasar por la caja reductora.
        </p>

        <h3>💪 Torque de entrada</h3>

        <p>
        Es el torque proporcionado por el motor al eje de
        entrada.
        </p>

        <h3>💪 Torque de salida</h3>

        <p>
        Es el torque disponible en el eje de salida después
        de considerar la relación de transmisión y la
        eficiencia.
        </p>

        <h3>📐 Relación de transmisión</h3>

        <p>
        Permite determinar cuánto se reduce la velocidad y
        cuánto se incrementa el torque.
        </p>

        <h3>📈 Eficiencia</h3>

        <p>
        Representa la proporción de potencia que se conserva
        durante la transmisión. En sistemas reales existen
        pérdidas debido principalmente a fricción, temperatura
        y otros factores mecánicos.
        </p>

        <h3>🔧 Ejemplo completo</h3>

        <p>
        Motor: <b>1800 RPM</b>
        </p>

        <p>
        Engranaje de entrada: <b>20 dientes</b>
        </p>

        <p>
        Engranaje de salida: <b>60 dientes</b>
        </p>

        <p>
        Relación: <b>3:1</b>
        </p>

        <p>
        Velocidad de salida:
        <b>1800 / 3 = 600 RPM</b>
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # CARGAR ESTILOS
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