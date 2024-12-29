import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt6.QtCore import QThread, pyqtSignal

class ScriptRunner(QThread):
    output_signal = pyqtSignal(str)

    def __init__(self, script_path):
        QThread.__init__(self)
        self.script_path = script_path

    def run(self):
        try:
            process = subprocess.Popen(['python', self.script_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
            
            for line in iter(process.stdout.readline, ''):
                self.output_signal.emit(line.strip())
            
            process.stdout.close()
            return_code = process.wait()
            if return_code:
                raise subprocess.CalledProcessError(return_code, process.args)
        except subprocess.CalledProcessError as e:
            self.output_signal.emit(f"An error occurred:\n{e.stderr}")
        except FileNotFoundError:
            self.output_signal.emit(f"Script not found at {self.script_path}")

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Button to run the script
        self.run_button = QPushButton('Run Script')
        self.run_button.clicked.connect(self.run_script)
        layout.addWidget(self.run_button)

        # Text area for logging
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

        self.setLayout(layout)

        # Window settings
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Run Script with Real-Time Logging')
        
        self.show()

    def run_script(self):
        # Disable button while script is running
        self.run_button.setEnabled(False)

        self.update_log("Running script...")

        script_path = 'inline-audio.py'
        self.thread = ScriptRunner(script_path)
        self.thread.output_signal.connect(self.update_log)
        self.thread.finished.connect(self.script_finished)
        self.thread.start()

    def update_log(self, text):
        self.log_area.append(text)

    def script_finished(self):
        # Re-enable button after script completes
        self.run_button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())