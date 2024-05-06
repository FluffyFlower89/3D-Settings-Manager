# Global style variables
header = 'style="font-weight: bold; text-decoration: underline;"'
bodyTop = 'style="font-weight: bold;"'
bodyBot = 'style="font-style: italic;"'

class BaseSetting:
    """
    Base class for all graphics settings.

    Attributes:
        title (str): Title of the setting.
        options (list): List of options for the setting.
        tooltip_header (str): Header text for the tooltip.
        tooltip_body (str): Body text for the tooltip.
    """

    def __init__(self, title, options, tooltip_header, tooltip_body):
        """
        Initializes a graphics setting.

        Args:
            title (str): Title of the setting.
            options (list): List of options for the setting.
            tooltip_header (str): Header text for the tooltip.
            tooltip_body (str): Body text for the tooltip.
        """
        self.title = title
        self.options = options
        self.tooltip_header = tooltip_header
        self.tooltip_body = tooltip_body

    def get_title(self):
        """
        Gets the title of the setting.

        Returns:
            str: Title of the setting.
        """
        return self.title

    def get_options(self):
        """
        Gets the options of the setting.

        Returns:
            list: List of options for the setting.
        """
        return self.options

    def get_tooltip_header(self):
        """
        Gets the header text for the tooltip.

        Returns:
            str: Header text for the tooltip.
        """
        return self.tooltip_header

    def get_tooltip_body(self):
        """
        Gets the body text for the tooltip.

        Returns:
            str: Body text for the tooltip.
        """
        return self.tooltip_body

class D3D_Level(BaseSetting):
    """
    Class representing the D3D_Level setting.
    """

    def __init__(self):
        """
        Initializes the D3D Feature Level setting.
        """
        title = f'<p>D3D Feature Level&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Direct X 9.1", "Direct X 9.2", "Direct X 9.3", "Direct X 10.0", "Direct X 10.1", "Direct X 11.0", "Direct X 11.1", "Direct X 12.0", "Direct X 12.1"]
        tooltip_header = f'<h3 {header}>Select the maximum Direct X feature level:</h3>'
        tooltip_body = f'<p {bodyTop}>Override the maximum feature level that a D3D11 device can be created with. Setting this to a higher value may allow some applications to run that would otherwise fail to create a D3D11 device.</p><p {bodyBot}></p>'
        super().__init__(title, options, tooltip_header, tooltip_body)