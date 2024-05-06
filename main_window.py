from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSplitter
from settings_panel import SettingsPanel
from app_list_panel import AppListPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphics Settings Manager")

        # Create main layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Create splitter
        splitter = QSplitter()
        layout.addWidget(splitter)

        # Create app list panel and settings panel
        self.app_list_panel = AppListPanel()
        self.settings_panel = SettingsPanel()

        # Add panels to splitter
        splitter.addWidget(self.app_list_panel)
        splitter.addWidget(self.settings_panel)

        # Set sizes for the splitter
        splitter.setSizes([400, 600])  # Adjust the sizes as needed
