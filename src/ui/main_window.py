from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from src.models.motor import Motor
from src.models.gearbox import Gearbox
from src.models.simulation import Simulation


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        self.setWindowTitle("MotoEléctric 3D")
        self.resize(1000, 650)

        self.create_interface()

    def create_interface(self):

        # ==========================================
        # TÍTULO
        # ==========================================

        title = QLabel("MOTOELÉCTRIC 3D")
        title.setObjectName("title")

        subtitle = QLabel(
            "Simulador de motores eléctricos y cajas reductoras"
        )
        subtitle.setObjectName("subtitle")

        # ==========================================
        # FORMULARIO DEL MOTOR
        # ==========================================

        motor_group = QGroupBox("Configuración del motor")

        motor_layout = QFormLayout()

        self.power_input = QLineEdit()
        self.power_input.setPlaceholderText("Ejemplo: 2200")

        self.rpm_input = QLineEdit()
        self.rpm_input.setPlaceholderText("Ejemplo: 1800")

        self.voltage_input = QLineEdit()
        self.voltage_input.setPlaceholderText("Ejemplo: 220")

        self.current_input = QLineEdit()
        self.current_input.setPlaceholderText("Ejemplo: 10")

        motor_layout.addRow("Potencia (W):", self.power_input)
        motor_layout.addRow("RPM:", self.rpm_input)
        motor_layout.addRow("Voltaje (V):", self.voltage_input)
        motor_layout.addRow("Corriente (A):", self.current_input)

        motor_group.setLayout(motor_layout)

        # ==========================================
        # FORMULARIO DE LA CAJA
        # ==========================================

        gearbox_group = QGroupBox("Configuración de la caja")

        gearbox_layout = QFormLayout()

        self.input_teeth = QLineEdit()
        self.input_teeth.setPlaceholderText("Ejemplo: 20")

        self.output_teeth = QLineEdit()
        self.output_teeth.setPlaceholderText("Ejemplo: 60")

        self.efficiency_input = QLineEdit()
        self.efficiency_input.setPlaceholderText("Ejemplo: 90")

        gearbox_layout.addRow(
            "Dientes entrada:",
            self.input_teeth
        )

        gearbox_layout.addRow(
            "Dientes salida:",
            self.output_teeth
        )

        gearbox_layout.addRow(
            "Eficiencia (%):",
            self.efficiency_input
        )

        gearbox_group.setLayout(gearbox_layout)

        # ==========================================
        # BOTÓN SIMULAR
        # ==========================================

        self.simulate_button = QPushButton("SIMULAR")

        self.simulate_button.clicked.connect(
            self.run_simulation
        )

        # ==========================================
        # PANEL DE RESULTADOS
        # ==========================================

        result_group = QGroupBox("Resultados")

        result_layout = QFormLayout()

        self.input_rpm_result = QLabel("-")
        self.input_torque_result = QLabel("-")
        self.ratio_result = QLabel("-")
        self.output_rpm_result = QLabel("-")
        self.output_torque_result = QLabel("-")
        self.efficiency_result = QLabel("-")

        result_layout.addRow(
            "RPM entrada:",
            self.input_rpm_result
        )

        result_layout.addRow(
            "Torque entrada:",
            self.input_torque_result
        )

        result_layout.addRow(
            "Relación:",
            self.ratio_result
        )

        result_layout.addRow(
            "RPM salida:",
            self.output_rpm_result
        )

        result_layout.addRow(
            "Torque salida:",
            self.output_torque_result
        )

        result_layout.addRow(
            "Eficiencia:",
            self.efficiency_result
        )

        result_group.setLayout(result_layout)

        # ==========================================
        # COLUMNA IZQUIERDA
        # ==========================================

        left_layout = QVBoxLayout()

        left_layout.addWidget(motor_group)
        left_layout.addWidget(gearbox_group)
        left_layout.addWidget(self.simulate_button)
        left_layout.addStretch()

        # ==========================================
        # COLUMNA DERECHA
        # ==========================================

        right_layout = QVBoxLayout()

        right_layout.addWidget(result_group)
        right_layout.addStretch()

        # ==========================================
        # CONTENEDOR PRINCIPAL
        # ==========================================

        columns_layout = QHBoxLayout()

        columns_layout.addLayout(left_layout, 1)
        columns_layout.addLayout(right_layout, 1)

        # ==========================================
        # LAYOUT PRINCIPAL
        # ==========================================

        main_layout = QVBoxLayout()

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)
        main_layout.addLayout(columns_layout)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

        # ==========================================
        # ESTILOS
        # ==========================================

        self.setStyleSheet("""
            QMainWindow {
                background-color: #d1d5db;
            }

            QLabel#title {
                font-size: 28px;
                font-weight: bold;
                color: #6495ED;
                padding-top: 15px;
            }

            QLabel#subtitle {
                font-size: 14px;
                color: #6495ED;
                padding-bottom: 15px;
            }

            QGroupBox {
                background-color: #A9A9A9;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                margin-top: 10px;
                padding: 15px;
                font-size: 15px;
                font-weight: bold;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }

            QLineEdit {
                background-color: #f9fafb;
                color: #1e40af;
                border: 2px solid #93c5fd;
                border-radius: 6px;
                padding: 8px;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 1px solid #2563eb;
            }

            QPushButton {
                background-color: #2563eb;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }
        """)

    # ==========================================
    # EJECUTAR SIMULACIÓN
    # ==========================================

    def run_simulation(self):

        try:

            power = float(
                self.power_input.text()
            )

            rpm = float(
                self.rpm_input.text()
            )

            voltage = float(
                self.voltage_input.text()
            )

            current = float(
                self.current_input.text()
            )

            input_teeth = int(
                self.input_teeth.text()
            )

            output_teeth = int(
                self.output_teeth.text()
            )

            efficiency = float(
                self.efficiency_input.text()
            ) / 100

            # Validaciones

            if power <= 0:
                raise ValueError(
                    "La potencia debe ser mayor que 0."
                )

            if rpm <= 0:
                raise ValueError(
                    "Las RPM deben ser mayores que 0."
                )

            if voltage <= 0:
                raise ValueError(
                    "El voltaje debe ser mayor que 0."
                )

            if current <= 0:
                raise ValueError(
                    "La corriente debe ser mayor que 0."
                )

            if input_teeth <= 0:
                raise ValueError(
                    "Los dientes de entrada deben ser mayores que 0."
                )

            if output_teeth <= 0:
                raise ValueError(
                    "Los dientes de salida deben ser mayores que 0."
                )

            if efficiency <= 0 or efficiency > 1:
                raise ValueError(
                    "La eficiencia debe estar entre 1 y 100%."
                )

            # ==================================
            # CREAR MOTOR
            # ==================================

            motor = Motor(
                voltage=voltage,
                current=current,
                rpm=rpm,
                power=power
            )

            # ==================================
            # CREAR CAJA
            # ==================================

            gearbox = Gearbox(
                input_teeth=input_teeth,
                output_teeth=output_teeth,
                efficiency=efficiency
            )

            # ==================================
            # EJECUTAR SIMULACIÓN
            # ==================================

            simulation = Simulation(
                motor,
                gearbox
            )

            result = simulation.run()

            # ==================================
            # MOSTRAR RESULTADOS
            # ==================================

            self.input_rpm_result.setText(
                f"{result['input_rpm']:.2f} RPM"
            )

            self.input_torque_result.setText(
                f"{result['input_torque']:.2f} Nm"
            )

            self.ratio_result.setText(
                f"{result['ratio']:.2f}:1"
            )

            self.output_rpm_result.setText(
                f"{result['output_rpm']:.2f} RPM"
            )

            self.output_torque_result.setText(
                f"{result['output_torque']:.2f} Nm"
            )

            self.efficiency_result.setText(
                f"{result['efficiency'] * 100:.1f}%"
            )

        except ValueError as error:

            QMessageBox.warning(
                self,
                "Datos incorrectos",
                str(error)
            )