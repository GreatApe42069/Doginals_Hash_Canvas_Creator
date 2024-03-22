from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit, QWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon

import subprocess
import json
import sys
import os


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

        # Set window icon
        self.setWindowIcon(QIcon('C:/DoginalsHashCanvasCreator/IMG_155.png'))

        # Initialize thread
        self.thread = None

        self.initUI()

    def initUI(self):
        # Create buttons
        self.btnEncoder = QPushButton('Run Encoder', self)
        self.btnDecoder = QPushButton('Run Decoder', self)
        self.btnColorBlockGenerator = QPushButton('Background Color Block Generator', self)
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
        self.inputImagePathEncoder.setPlaceholderText("Enter image path or paths seperated by a comma for Encoding")
        self.inputImagePathEncoder.setFixedWidth(800)
        layout.addWidget(self.inputImagePathEncoder)

        # Input field for hidden message for encoder
        self.inputHiddenMessageEncoder = QLineEdit(self)
        self.inputHiddenMessageEncoder.setPlaceholderText("Enter hidden message or messages seperated by commas for Encoding")
        self.inputHiddenMessageEncoder.setFixedWidth(800)
        layout.addWidget(self.inputHiddenMessageEncoder)

        layout.addWidget(self.btnColorBlockGenerator)

        # Input field for transaction IDs and hidden messages for Color Block Generator
        self.inputTransactionIDsColorBlock = QLineEdit(self)
        self.inputTransactionIDsColorBlock.setPlaceholderText("Enter transaction ID or IDs separated by commas")
        self.inputTransactionIDsColorBlock.setFixedWidth(800)
        layout.addWidget(self.inputTransactionIDsColorBlock)

        self.inputHiddenMessagesColorBlock = QLineEdit(self)
        self.inputHiddenMessagesColorBlock.setPlaceholderText("Enter hidden message or messages separated by commas")
        self.inputHiddenMessagesColorBlock.setFixedWidth(800)
        layout.addWidget(self.inputHiddenMessagesColorBlock)

        layout.addWidget(self.btnHashMapGenerator)

        # Input field for transaction IDs and hidden messages for Hash-map Generator
        self.inputTransactionIDsHashMap = QLineEdit(self)
        self.inputTransactionIDsHashMap.setPlaceholderText("Enter transaction ID or IDs separated by commas")
        self.inputTransactionIDsHashMap.setFixedWidth(800)
        layout.addWidget(self.inputTransactionIDsHashMap)

        self.inputHiddenMessagesHashMap = QLineEdit(self)
        self.inputHiddenMessagesHashMap.setPlaceholderText("Enter hidden message or messages separated by commas")
        self.inputHiddenMessagesHashMap.setFixedWidth(800)
        layout.addWidget(self.inputHiddenMessagesHashMap)

        layout.addWidget(self.btnSuperCanvasGenerator)

        # Input field for transaction IDs and hidden messages for Super Canvas Generator
        self.inputTransactionIDsSuperCanvas = QLineEdit(self)
        self.inputTransactionIDsSuperCanvas.setPlaceholderText("Enter transaction ID or IDs separated by commas")
        self.inputTransactionIDsSuperCanvas.setFixedWidth(800)
        layout.addWidget(self.inputTransactionIDsSuperCanvas)

        self.inputHiddenMessagesSuperCanvas = QLineEdit(self)
        self.inputHiddenMessagesSuperCanvas.setPlaceholderText("Enter hidden message or messages separated by commas")
        self.inputHiddenMessagesSuperCanvas.setFixedWidth(800)
        layout.addWidget(self.inputHiddenMessagesSuperCanvas)

        # Set the layout for the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

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
        # Get the image path from the input field
        image_path = self.inputImagePathDecoder.text()

        if not image_path:
            # If the input field is empty, open the file dialog to select an image
            image_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Image files (*.jpg *.png)')
            self.inputImagePathDecoder.setText(image_path)

        # Validate input
        if not image_path:
            QMessageBox.warning(self, "Warning", "Please select an image for Decoder.")
            return

        # Run subprocess to decode the hidden message
        self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\Hidden_Extractor.exe'], input_data=image_path)

    def runEncoder(self):
        # Get the image path or paths from the input field
        image_paths = self.inputImagePathEncoder.text().split(',')
        if not image_paths:
            QMessageBox.warning(self, "Warning", "Please enter image path(s) for encoder.")
            return

        # Get the hidden message or messages from the input field
        hidden_messages = self.inputHiddenMessageEncoder.text().split(',')
        if not hidden_messages:
            QMessageBox.warning(self, "Warning", "Please enter hidden message(s) for encoder.")
            return

        # Validate that the number of files matches the number of messages
        if len(image_paths) != len(hidden_messages):
            QMessageBox.warning(self, "Warning", "Number of image paths must match number of hidden messages.")
            return

        # Iterate over each image path and hidden message
        for image_path, hidden_message in zip(image_paths, hidden_messages):
            # Validate the existence of the image file
            if not os.path.isfile(image_path.strip()):  # Trim leading/trailing whitespace
                QMessageBox.warning(self, "Warning", f"File does not exist: {image_path}")
                return

            # Run subprocess to encode the hidden message for the current file
            self.runSubprocess([r'C:\DoginalsHashCanvasCreator\dist\Hidden_Encoder.exe'], input_data=f"{image_path.strip()}\n{hidden_message.strip()}")

        # Notify the user that encoding is complete
        QMessageBox.information(self, "Information", "Encoding complete for all files.")

    # Inside the runColorBlockGenerator function (similar changes can be applied to other generator functions)
    def runColorBlockGenerator(self):
        transaction_ids_input = self.inputTransactionIDsColorBlock.text()
        hidden_messages_input = self.inputHiddenMessagesColorBlock.text()

        # Split the input transaction IDs and hidden messages
        transaction_ids = transaction_ids_input.split(',')
        hidden_messages = hidden_messages_input.split(',')

        # Validate input
        if len(transaction_ids) != len(hidden_messages):
            QMessageBox.warning(self, "Warning", "Number of transaction IDs must match number of hidden messages.")
            return

        # Read the existing data from transaction_ids.json
        with open('transaction_ids.json', 'r') as json_file:
            existing_data = json.load(json_file)

        # Create a list of dictionaries containing transaction IDs and hidden messages
        new_data = [{"TransactionID": tid.strip(), "HiddenMessage": msg.strip()} for tid, msg in zip(transaction_ids, hidden_messages)]

        # Append the new data to the existing data
        all_data = new_data

        # Write the combined data back to transaction_ids.json
        with open("transaction_ids.json", "w") as json_file:
            json.dump(all_data, json_file, indent=4)

        # Run subprocess for color block generator
        self.runSubprocess(['python', r'C:\DoginalsHashCanvasCreator\auto_doginals_hash_canvas_creator.py'])

        # Notify the user that encoding is complete
        QMessageBox.information(self, "Information", "Created and Encoded!")


    def runHashMapGenerator(self):
        transaction_ids_input = self.inputTransactionIDsColorBlock.text()
        hidden_messages_input = self.inputHiddenMessagesColorBlock.text()

        # Split the input transaction IDs and hidden messages
        transaction_ids = transaction_ids_input.split(',')
        hidden_messages = hidden_messages_input.split(',')

        # Validate input
        if len(transaction_ids) != len(hidden_messages):
            QMessageBox.warning(self, "Warning", "Number of transaction IDs must match number of hidden messages.")
            return

        # Read the existing data from transaction_ids.json
        with open('transaction_ids.json', 'r') as json_file:
            existing_data = json.load(json_file)

        # Create a list of dictionaries containing transaction IDs and hidden messages
        new_data = [{"TransactionID": tid.strip(), "HiddenMessage": msg.strip()} for tid, msg in zip(transaction_ids, hidden_messages)]

        # Append the new data to the existing data
        all_data = new_data

        # Write the combined data back to transaction_ids.json
        with open("transaction_ids.json", "w") as json_file:
            json.dump(all_data, json_file, indent=4)

        # Run subprocess for color block generator
        self.runSubprocess(['python', r'C:\DoginalsHashCanvasCreator\auto_doginals_hash_canvas_creator_unique-shapes.py'])

        # Notify the user that encoding is complete
        QMessageBox.information(self, "Information", "Encoding complete for all files.")


    def runSuperCanvasGenerator(self):
        transaction_ids_input = self.inputTransactionIDsColorBlock.text()
        hidden_messages_input = self.inputHiddenMessagesColorBlock.text()

        # Split the input transaction IDs and hidden messages
        transaction_ids = transaction_ids_input.split(',')
        hidden_messages = hidden_messages_input.split(',')

        # Validate input
        if len(transaction_ids) != len(hidden_messages):
            QMessageBox.warning(self, "Warning", "Number of transaction IDs must match number of hidden messages.")
            return

        # Read the existing data from transaction_ids.json
        with open('transaction_ids.json', 'r') as json_file:
            existing_data = json.load(json_file)

        # Create a list of dictionaries containing transaction IDs and hidden messages
        new_data = [{"TransactionID": tid.strip(), "HiddenMessage": msg.strip()} for tid, msg in zip(transaction_ids, hidden_messages)]

        # Append the new data to the existing data
        all_data = new_data

        # Write the combined data back to transaction_ids.json
        with open("transaction_ids.json", "w") as json_file:
            json.dump(all_data, json_file, indent=4)

        # Run subprocess for color block generator
        self.runSubprocess(['python', r'C:\DoginalsHashCanvasCreator\auto_super_canvas_creator.py'])

        # Notify the user that encoding is complete
        QMessageBox.information(self, "Information", "Encoding complete for all files.")

if __name__ == "__main__":
    app = QApplication([])
    window = YourApp()
    window.show()
    sys.exit(app.exec_())
