from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QFileDialog, \
    QLineEdit, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import sys
import os
import subprocess

class SubprocessThread(QThread):
    finished = pyqtSignal()

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        try:
            process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout, stderr = process.communicate(input=self.input_data.encode())
            self.output = stdout.decode() + stderr.decode()
        except Exception as e:
            print(f"Error running subprocess: {e}")
        finally:
            self.finished.emit()

class YourApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Node Runners Doginal Decoder')
        self.setGeometry(100, 100, 800, 600)

        # Set dark theme
        self.setDarkTheme()

        # Create image viewer
        self.imageLabel = QLabel(self)
        self.imageLabel.setFixedSize(400, 400)

        # Input field for file name
        self.inputFileName = QLineEdit(self)
        self.inputFileName.setPlaceholderText("Enter file name")
        self.inputFileName.setFixedWidth(200)

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
        layout.addWidget(self.btnEncoder)
        layout.addWidget(self.btnDecoder)
        layout.addWidget(self.inputFileName)  # Add input field to layout
        layout.addWidget(self.btnColorBlockGenerator)
        layout.addWidget(self.btnHashMapGenerator)
        layout.addWidget(self.btnSuperCanvasGenerator)
        layout.addWidget(self.imageLabel)

        # Set the layout for the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def setDarkTheme(self):
        # Set dark theme with gray background
        style = """
            QMainWindow {background: #303030; color: #E0E0E0}
            QPushButton {background-color: #484848; color: #E0E0E0; border: 1px solid #E0E0E0;}
            QPushButton:hover {background-color: #686868}
            QLabel {color: #E0E0E0}
            QLineEdit {background-color: #484848; color: #E0E0E0; border: 1px solid #E0E0E0;}
        """

        self.setStyleSheet(style)

        # Set dark theme for file dialog
        self.setStyleSheet("QFileDialog {background-color: #303030; color: #E0E0E0;}")

    def runSubprocess(self, command, input_data=""):
        # Ensure any existing thread is finished before starting a new one
        if self.thread and self.thread.isRunning():
            self.thread.wait()
            self.thread = None

        self.thread = SubprocessThread(command)
        self.thread.input_data = input_data
        self.thread.finished.connect(self.handleSubprocessFinished)
        self.thread.start()

    def handleSubprocessFinished(self):
        # This slot is called when the subprocess thread finishes
        # You can update the UI or perform other tasks here
        pass

    def runEncoder(self):
        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\Hidden_Encoder.exe'])

    def runDecoder(self):
        file_name = self.inputFileName.text()  # Get the file name from the input field
        if not file_name:
            QMessageBox.warning(self, "Warning", "Please enter a file name.")
            return

        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\Hidden_Extractor.exe'], input_data=file_name)

    def runColorBlockGenerator(self):
        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\auto_doginals_hash_canvas_creator.exe'])

    def runHashMapGenerator(self):
        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\hash_map_generator.exe'])

    def runSuperCanvasGenerator(self):
        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\super_canvas_generator.exe'])

    def saveImage(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;All Files (*)")

        if save_path:
            # Specify the file to copy, not the directory
            image_path = r"C:\DoginalsHashCanvasCreator\super-canvas_generated_images\generated_image_steg.png"
            os.system(f'copy "{image_path}" "{save_path}"')
            print(f"Image saved to {save_path}")

if __name__ == "__main__":
    app = QApplication([])
    window = YourApp()
    window.show()
    sys.exit(app.exec_())
