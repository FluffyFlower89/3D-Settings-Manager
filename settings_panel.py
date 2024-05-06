from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QScrollArea, QFrame, QPushButton
from Settings import *

class SettingsPanel(QWidget):
    def __init__(self):
        """
        Initializes the SettingsPanel widget.

        Args:
            None

        Returns:
            None
        """
        super().__init__()

        # Set up the scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.setLayout(QVBoxLayout())
        self.label = QLabel("Settings")
        self.layout().addWidget(self.label)
        self.layout().addWidget(scroll_area)

        # Create the settings widget
        self.settings_widget = QWidget()
        scroll_area.setWidget(self.settings_widget)
        self.settings_layout = QVBoxLayout(self.settings_widget)
        self.settings_widget.setLayout(self.settings_layout)

        # Dictionary to store comboboxes and their IDs
        self.comboboxes = {}

        # List of setting classes
        setting_classes = [
            FXAA(),                         #ID - 00 
            FXAA_Quality_Subpixel(),        #ID - 01
            FXAA_Quality_Edge_Threshold(),  #ID - 02
            FXAA_Edge_Threshold_Bias(),     #ID - 03
            SMAA(),                         #ID - 04
            SMAA_Edge_Detection(),          #ID - 05
            SMAA_Threshold(),               #ID - 06
            SMAA_Search_Steps(),            #ID - 07
            SMAA_Search_Steps_Diagonal(),   #ID - 08
            SMAA_Corner_Rounding(),         #ID - 09
            CAS(),                          #ID - 10
            DLS_Sharpness(),                #ID - 11
            DLS_Denoise(),                  #ID - 12
            VSYNC(),                        #ID - 13
            Frame_Limit(),                  #ID - 14
            VSYNC_D3D9(),                   #ID - 15
            Frame_Limit_D3D9(),             #ID - 16
            Anistropic_Filtering(),         #ID - 17
            LOD_Bias(),                     #ID - 18
            Clamp_Negative_LOD(),           #ID - 19
            Anistropic_Filtering_D3D9(),    #ID - 20
            LOD_Bias_D3D9(),                #ID - 21
            Clamp_Negative_LOD_D3D9(),      #ID - 22
            HDR(),                          #ID - 23
            D3D_Level()                     #ID - 24
            ]

        # Populate the settings
        self.populate_settings(setting_classes)

        # Add save button
        self.add_app_button = QPushButton("Save Settings")
        self.layout().addWidget(self.add_app_button)

    def populate_settings(self, setting_classes):
        """
        Populates the settings panel with the provided setting classes.

        Args:
            setting_classes (list): List of setting classes to populate the panel with.

        Returns:
            None
        """
        for setting_class in setting_classes:
            title = setting_class.get_title()
            options = setting_class.get_options()
            tooltip_header = setting_class.get_tooltip_header()
            tooltip_body = setting_class.get_tooltip_body()
            self.add_setting(title, options, tooltip_header, tooltip_body)

    def add_setting(self, title, options, tooltip_header, tooltip_body):
        """
        Adds a setting to the settings panel.

        Args:
            title (str): Title of the setting.
            options (list): List of options for the setting.
            tooltip_header (str): Header text for the tooltip.
            tooltip_body (str): Body text for the tooltip.

        Returns:
            None
        """
        container = QWidget()
        container_layout = QVBoxLayout(container)

        # Create label
        label = QLabel(f'<html><body>{title}</body></html>')

        # Create combobox
        combobox = QComboBox()
        combobox.addItems(options)

        # Set tooltip for label
        label.setToolTip(f'<html><body>{tooltip_header}{tooltip_body}</body></html>')
        
        container_layout.addWidget(label)
        container_layout.addWidget(combobox)

        # Add horizontal rule after specific combobox indices
        hr = QFrame()
        hr.setFrameShape(QFrame.Shape.HLine)
        hr.setFrameShadow(QFrame.Shadow.Plain)
        
        if (len(self.settings_layout) == 3 or 
            len(self.settings_layout) == 9 or 
            len(self.settings_layout) == 10 or 
            len(self.settings_layout) == 12 or 
            len(self.settings_layout) == 16 or 
            len(self.settings_layout) == 22 or 
            len(self.settings_layout) == 23):
            container_layout.addWidget(hr)

        self.settings_layout.addWidget(container)

        # Assign an ID to the combobox and store it in the dictionary
        combobox_id = len(self.comboboxes)
        combobox.setProperty("id", combobox_id)
        self.comboboxes[combobox_id] = combobox

        # Connect the combobox signal to the function for enabling or disabling other comboboxes
        combobox.currentIndexChanged.connect(self.toggle_comboboxes)

        # Disable specific comboboxes initially
        if combobox_id in [1, 2, 3, 5, 6, 7, 8, 9]:
            combobox.setEnabled(False)

    def toggle_comboboxes(self, index):
        """
        Toggles the state of comboboxes based on the index of the selected item.

        Args:
            index (int): Index of the selected item in the combobox.

        Returns:
            None
        """
        # Get the combobox that emitted the signal
        sender_combobox = self.sender()
        # Get the combobox ID
        combobox_id = sender_combobox.property("id")

        # Determine which comboboxes to activate based on the sender_combobox
        if combobox_id == 0 and index == 1:
            for id in range(1, 4):
                self.comboboxes[id].setEnabled(True)
        elif combobox_id == 0 and index in [0, 2]:
            for id in range(1, 4):
                self.comboboxes[id].setEnabled(False)
        elif combobox_id == 4 and index == 1:
            for id in range(5, 10):
                self.comboboxes[id].setEnabled(True)
        elif combobox_id == 4 and index in [0, 2]:
            for id in range(5, 10):
                self.comboboxes[id].setEnabled(False)
        elif combobox_id == 13 and index in [1, 2]:
            self.comboboxes[15].setEnabled(False)
        elif combobox_id == 13 and index in [0, 3]:
            self.comboboxes[15].setEnabled(True)
        elif combobox_id == 15 and index in [1, 2]:
            self.comboboxes[13].setEnabled(False)
        elif combobox_id == 15 and index in [0, 3]:
            self.comboboxes[13].setEnabled(True)
        elif combobox_id == 14 and index in [1, 2, 3, 4, 5, 6]:
            self.comboboxes[16].setEnabled(False)
        elif combobox_id == 14 and index in [0, 7]:
            self.comboboxes[16].setEnabled(True)
        elif combobox_id == 16 and index in [1, 2, 3, 4, 5, 6]:
            self.comboboxes[14].setEnabled(False)
        elif combobox_id == 16 and index in [0, 7]:
            self.comboboxes[14].setEnabled(True)