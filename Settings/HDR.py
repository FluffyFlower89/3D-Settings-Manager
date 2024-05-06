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

class HDR(BaseSetting):
    """
    Class representing the HDR (High Dynamic Range) setting.
    """

    def __init__(self):
        """
        Initializes the HDR setting.
        """
        title = f'<p>HDR - High Dynamic Range&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Enabled", "Disabled"]
        tooltip_header = f'<h3 {header}>Select whether to enable or disable HDR:</h3>'
        tooltip_body = f'<p {bodyTop}>High Dynamic Range (HDR) enhances visual quality by expanding the range of brightness and contrast levels, resulting in more vibrant and realistic images.</p><p {bodyBot}>This shows to the game that the global Windows "HDR Mode" is enabled. Many (broken) games will need this to be set to consider exposing HDR output as determine it based on the DXGIOutputs current ColorSpace instead of using CheckColorSpaceSupport.<br>This will not enable HDR for Games that dont support it!!</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)