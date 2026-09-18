from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTabWidget,
    QTextEdit,
    QFrame
)


class MotorsWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "MotoEléctric 3D - Motores eléctricos"
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

        title = QLabel("⚡ MOTORES ELÉCTRICOS")
        title.setObjectName("title")

        subtitle = QLabel(
            "Conoce el funcionamiento, componentes y "
            "principales características de los motores eléctricos."
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
            "🔩 Componentes"
        )

        tabs.addTab(
            self.create_types_tab(),
            "⚙ Tipos"
        )

        tabs.addTab(
            self.create_operation_tab(),
            "⚡ Funcionamiento"
        )

        tabs.addTab(
            self.create_variables_tab(),
            "📊 Variables"
        )

        main_layout.addWidget(tabs)

        central_widget.setLayout(main_layout)

    # ==========================================
    # PESTAÑA INTRODUCCIÓN
    # ==========================================

    def create_introduction_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)

        title = QLabel(
            "¿Qué es un motor eléctrico?"
        )

        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>Motor eléctrico</h2>

        <p>
        Un <b>motor eléctrico</b> es una máquina que transforma
        energía eléctrica en energía mecánica mediante la
        interacción de campos magnéticos.
        </p>

        <p>
        Los motores eléctricos son utilizados en una gran
        variedad de aplicaciones, desde pequeños dispositivos
        electrónicos hasta vehículos eléctricos, máquinas
        industriales y sistemas de automatización.
        </p>

        <h3>¿Por qué son importantes?</h3>

        <p>
        Los motores permiten convertir la energía eléctrica
        disponible en una forma de movimiento que puede ser
        utilizada para realizar diferentes tipos de trabajo.
        </p>

        <h3>Principales características</h3>

        <ul>
            <li>Transforman energía eléctrica en energía mecánica.</li>
            <li>Producen movimiento rotacional.</li>
            <li>Poseen diferentes velocidades de operación.</li>
            <li>Su funcionamiento depende de campos magnéticos.</li>
            <li>Pueden utilizarse en diferentes sistemas mecánicos.</li>
        </ul>

        <h3>Aplicaciones</h3>

        <ul>
            <li>Vehículos eléctricos.</li>
            <li>Bombas.</li>
            <li>Ventiladores.</li>
            <li>Robótica.</li>
            <li>Maquinaria industrial.</li>
            <li>Sistemas de automatización.</li>
        </ul>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # PESTAÑA COMPONENTES
    # ==========================================

    def create_components_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)

        title = QLabel(
            "Componentes principales"
        )

        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>Partes de un motor eléctrico</h2>

        <p>
        Aunque existen diferentes tipos de motores,
        muchos comparten elementos fundamentales.
        </p>

        <h3>🔩 Estator</h3>

        <p>
        Es la parte fija del motor. Contiene elementos
        electromagnéticos que permiten generar el campo
        magnético necesario para producir el movimiento.
        </p>

        <h3>⚙ Rotor</h3>

        <p>
        Es la parte móvil del motor. Gira debido a la
        interacción entre los campos magnéticos del rotor
        y del estator.
        </p>

        <h3>🔄 Eje</h3>

        <p>
        El eje transmite el movimiento de rotación generado
        por el rotor hacia el sistema mecánico conectado
        al motor.
        </p>

        <h3>🧲 Bobinas</h3>

        <p>
        Las bobinas generan campos magnéticos cuando circula
        corriente eléctrica a través de ellas.
        </p>

        <h3>🛡 Carcasa</h3>

        <p>
        Protege los componentes internos y ayuda a mantener
        la estructura mecánica del motor.
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # PESTAÑA TIPOS
    # ==========================================

    def create_types_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)

        title = QLabel(
            "Principales tipos de motores"
        )

        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>Clasificación de motores eléctricos</h2>

        <h3>⚡ Motor de corriente continua (DC)</h3>

        <p>
        Funciona utilizando corriente continua. Son utilizados
        en aplicaciones donde se requiere un control sencillo
        de velocidad y torque.
        </p>

        <h3>🔌 Motor de corriente alterna (AC)</h3>

        <p>
        Utiliza corriente alterna y es ampliamente empleado
        en aplicaciones industriales.
        </p>

        <h3>🔄 Motor de inducción</h3>

        <p>
        Es uno de los motores más utilizados en la industria.
        Su funcionamiento se basa en la inducción electromagnética.
        </p>

        <h3>🎯 Motor síncrono</h3>

        <p>
        Su velocidad de rotación se mantiene sincronizada
        con la frecuencia del campo magnético aplicado.
        </p>

        <h3>🚗 Motores utilizados en vehículos eléctricos</h3>

        <p>
        Los vehículos eléctricos pueden utilizar diferentes
        tecnologías de motores, entre ellas motores síncronos
        de imanes permanentes y motores de inducción.
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # PESTAÑA FUNCIONAMIENTO
    # ==========================================

    def create_operation_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)

        title = QLabel(
            "¿Cómo funciona un motor eléctrico?"
        )

        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>Principio de funcionamiento</h2>

        <p>
        El funcionamiento de un motor eléctrico está relacionado
        con la interacción entre campos magnéticos y corriente
        eléctrica.
        </p>

        <h3>1. Aplicación de energía</h3>

        <p>
        Se suministra energía eléctrica al motor mediante una
        fuente de alimentación.
        </p>

        <h3>2. Generación del campo magnético</h3>

        <p>
        La corriente eléctrica produce campos magnéticos en
        los componentes electromagnéticos del motor.
        </p>

        <h3>3. Interacción magnética</h3>

        <p>
        Los campos magnéticos interactúan generando una fuerza
        que produce el movimiento del rotor.
        </p>

        <h3>4. Generación de torque</h3>

        <p>
        El movimiento producido genera un torque que puede
        transmitirse mediante el eje hacia otro componente
        mecánico.
        </p>

        <h3>5. Transmisión del movimiento</h3>

        <p>
        El eje puede conectarse directamente a una carga o
        utilizar una caja reductora para modificar la velocidad
        y el torque.
        </p>
        """)

        layout.addWidget(title)
        layout.addWidget(content)

        widget.setLayout(layout)

        return widget

    # ==========================================
    # PESTAÑA VARIABLES
    # ==========================================

    def create_variables_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)

        title = QLabel(
            "Variables importantes"
        )

        title.setObjectName("sectionTitle")

        content = QTextEdit()
        content.setReadOnly(True)

        content.setHtml("""
        <h2>Variables utilizadas en la simulación</h2>

        <h3>⚡ Voltaje (V)</h3>

        <p>
        Representa la diferencia de potencial eléctrico aplicada
        al motor. Su unidad es el voltio (V).
        </p>

        <h3>🔌 Corriente (A)</h3>

        <p>
        Representa el flujo de carga eléctrica. Se mide en
        amperios (A).
        </p>

        <h3>🔥 Potencia (W)</h3>

        <p>
        Representa la cantidad de energía utilizada o entregada
        por unidad de tiempo. Se mide en vatios (W).
        </p>

        <h3>🔄 RPM</h3>

        <p>
        Significa revoluciones por minuto y representa la
        velocidad de rotación del motor.
        </p>

        <h3>💪 Torque (Nm)</h3>

        <p>
        Representa la capacidad del motor para producir
        movimiento de rotación. Se mide en Newton-metro (Nm).
        </p>

        <h3>📈 Eficiencia (%)</h3>

        <p>
        Representa qué proporción de la energía suministrada
        se convierte efectivamente en energía útil.
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