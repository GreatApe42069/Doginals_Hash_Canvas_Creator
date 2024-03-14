from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit, QWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
import subprocess
import json
import sys

class SubprocessThread(QThread):
    finished = pyqtSignal()

    def __init__(self, command, input_data=""):
        super().__init__()
        self.command = command
        self.input_data = input_data

    def run(self):
        try:
            process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout, stderr = process.communicate(input=self.input_data.encode())
            self.output = stdout.decode() + stderr.decode()
        except Exception as e:
            print(f"Error running subprocess: {e}")
        finally:
            self.finished.emit()

class HiddenMessageWindow(QWidget):
    def __init__(self, hidden_message):
        super().__init__()
        self.setWindowTitle('Hidden Message')
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()
        self.message_label = QLabel(hidden_message, self)
        layout.addWidget(self.message_label)

        self.setLayout(layout)

class YourApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Node Runners Doginal Decoder')
        self.setGeometry(100, 100, 800, 300)

        # Set dark theme
        self.setDarkTheme()

        # Initialize thread
        self.thread = None

        self.initUI()

    def initUI(self):
        # Create buttons
        self.btnEncoder = QPushButton('Run Encoder', self)
        self.btnDecoder = QPushButton('Run Decoder', self)
        self.btnColorBlockGenerator = QPushButton('Color Block Generator', self)
        self.btnHashMapGenerator = QPushButton('Hash-map Generator', self)
        self.btnSuperCanvasGenerator = QPushButton('Super Canvas Generator', self)

        # Connect buttons to functions
        self.btnEncoder.clicked.connect(self.runEncoder)
        self.btnDecoder.clicked.connect(self.runDecoder)
        self.btnColorBlockGenerator.clicked.connect(self.runColorBlockGenerator)
        self.btnHashMapGenerator.clicked.connect(self.runHashMapGenerator)
        self.btnSuperCanvasGenerator.clicked.connect(self.runSuperCanvasGenerator)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.btnDecoder)

        # Input field for image path for decoder
        self.inputImagePathDecoder = QLineEdit(self)
        self.inputImagePathDecoder.setPlaceholderText("Enter image path for decoder")
        self.inputImagePathDecoder.setFixedWidth(800)
        layout.addWidget(self.inputImagePathDecoder)

        layout.addWidget(self.btnEncoder)

        # Input field for image path for encoder
        self.inputImagePathEncoder = QLineEdit(self)
        self.inputImagePathEncoder.setPlaceholderText("Enter image path for encoder")
        self.inputImagePathEncoder.setFixedWidth(800)
        layout.addWidget(self.inputImagePathEncoder)

        layout.addWidget(self.btnColorBlockGenerator)

        # Input field for transaction IDs for Color Block Generator
        self.inputTransactionIDsColorBlock = QLineEdit(self)
        self.inputTransactionIDsColorBlock.setPlaceholderText("Enter transaction IDs for Color Block Generator")
        self.inputTransactionIDsColorBlock.setFixedWidth(800)
        layout.addWidget(self.inputTransactionIDsColorBlock)

        layout.addWidget(self.btnHashMapGenerator)

        # Input field for transaction IDs for Hash-map Generator
        self.inputTransactionIDsHashMap = QLineEdit(self)
        self.inputTransactionIDsHashMap.setPlaceholderText("Enter transaction IDs for Hash-map Generator")
        self.inputTransactionIDsHashMap.setFixedWidth(800)
        layout.addWidget(self.inputTransactionIDsHashMap)

        layout.addWidget(self.btnSuperCanvasGenerator)

        # Input field for transaction IDs for Super Canvas Generator
        self.inputTransactionIDsSuperCanvas = QLineEdit(self)
        self.inputTransactionIDsSuperCanvas.setPlaceholderText("Enter transaction IDs for Super Canvas Generator")
        self.inputTransactionIDsSuperCanvas.setFixedWidth(800)
        layout.addWidget(self.inputTransactionIDsSuperCanvas)

        # Set the layout for the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def setDarkTheme(self):
        # Set dark theme with black background
        style = """
            QMainWindow {background-color: #000000; color: #000000}
            QPushButton {background-color: #484848; color: #E0E0E0; border: 1px solid #E0E0E0;}
            QPushButton:hover {background-color: #686868}
            QLabel {color: #E0E0E0}
            QLineEdit {background-color: #484848; color: #E0E0E0; border: 1px solid #E0E0E0;}
            QMenuBar {background-color: #000000; color: #000000;}
            QMenuBar::item:selected {background-color: #686868;}
            QMenuBar::item:pressed {background-color: #484848;}
            QMenu {background-color: #484848; color: #E0E0E0;}
            QMenu::item:selected {background-color: #686868;}
        """

        self.setStyleSheet(style)

        # Set dark theme for file dialog
        self.setStyleSheet("QFileDialog {background-color: #303030; color: #E0E0E0;}")

    def runSubprocess(self, command, input_data=""):
        # Ensure any existing thread is finished before starting a new one
        if self.thread and self.thread.isRunning():
            self.thread.wait()
            self.thread = None

        self.thread = SubprocessThread(command, input_data)
        self.thread.finished.connect(self.handleSubprocessFinished)
        self.thread.start()

    def handleSubprocessFinished(self):
        # This slot is called when the subprocess thread finishes
        # You can update the UI or perform other tasks here
        if self.thread.command[0].endswith("Hidden_Extractor.exe"):
            # Decoder process finished, display the hidden message window
            hidden_message = self.thread.output.strip()
            if hidden_message:
                self.hidden_message_window = HiddenMessageWindow(hidden_message)
                self.hidden_message_window.show()
            else:
                QMessageBox.information(self, "Information", "No hidden message found in the image.")
        else:
            # Other subprocess finished, do nothing for now
            pass

    def runDecoder(self):
        image_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Image files (*.jpg *.png)')
        self.inputImagePathDecoder.setText(image_path)

        # Validate input
        if not image_path:
            QMessageBox.warning(self, "Warning", "Please select an image for decoder.")
            return

        # Run subprocess to decode the hidden message
        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\Hidden_Extractor.exe'], input_data=image_path)

    def runEncoder(self):
        image_path = self.inputImagePathEncoder.text()  # Get the image path from the input field
        if not image_path:
            QMessageBox.warning(self, "Warning", "Please enter an image path for encoder.")
            return

        # Run subprocess to encode the hidden message
        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\Hidden_Encoder.exe'], input_data=image_path)

    def runColorBlockGenerator(self):
        # Your implementation for runColorBlockGenerator goes here
        transaction_ids = self.inputTransactionIDsColorBlock.text()  
        # Get transaction IDs
        # Split the input transaction IDs and create a list of dictionaries
        transaction_list = [{"TransactionID": id} for id in transaction_ids.split()]

        # Save transaction IDs in JSON format
        with open("transaction_ids_color_block.json", "w") as json_file:
            json.dump(transaction_list, json_file, indent=4)

        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\auto_doginals_hash_canvas_creator.exe'])

    def runHashMapGenerator(self):
        transaction_ids = self.inputTransactionIDsHashMap.text()  # Get transaction IDs from the input field
        if not transaction_ids:
            QMessageBox.warning(self, "Warning", "Please enter transaction IDs for Hash-map Generator.")
            return

        # Split the input transaction IDs and create a list of dictionaries
        transaction_list = [{"TransactionID": id} for id in transaction_ids.split()]

        # Save transaction IDs in JSON format
        with open("transaction_ids_hash_map.json", "w") as json_file:
            json.dump(transaction_list, json_file, indent=4)

        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\hash_map_generator.exe'])

    def runSuperCanvasGenerator(self):
        transaction_ids = self.inputTransactionIDsSuperCanvas.text()  # Get transaction IDs from the input field
        if not transaction_ids:
            QMessageBox.warning(self, "Warning", "Please enter transaction IDs for Super Canvas Generator.")
            return

        # Split the input transaction IDs and create a list of dictionaries
        transaction_list = [{"TransactionID": id} for id in transaction_ids.split()]

        # Save transaction IDs in JSON format
        with open("transaction_ids_super_canvas.json", "w") as json_file:
            json.dump(transaction_list, json_file, indent=4)

        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\super_canvas_generator.exe'])

if __name__ == "__main__":
    app = QApplication([])
    window = YourApp()
    window.show()
    sys.exit(app.exec_())
