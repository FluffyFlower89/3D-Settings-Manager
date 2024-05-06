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

class CAS(BaseSetting):
    """
    Class representing the CAS (Contrast Adaptive Sharpening) setting.
    """

    def __init__(self):
        """
        Initializes the CAS setting.
        """
        title = f'<p>CAS - Contrast Adaptive Sharpening&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "1.00", "0.75", "0.50", "0.25", "0.00", "Off"]
        tooltip_header = f'<h3 {header}>Select the level of Adaptive Sharpening</h3>'
        tooltip_body = f'<p {bodyTop}>Contrast Adaptive Sharpening</p><p {bodyBot}>1.00 - Sharpest<br>0.75 - Sharp<br>0.50 - Medium<br>0.25 - Soft<br>0.00 - Softest</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)
