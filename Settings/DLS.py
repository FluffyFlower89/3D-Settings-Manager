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

class DLS_Sharpness(BaseSetting):
    """
    Class representing the DLS Sharpness setting.
    """

    def __init__(self):
        """
        Initializes the DLS Sharpness setting.
        """
        title = f'<p>DLS - Sharpness&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "1.00", "0.75", "0.50", "0.25", "0.00", "Off"]
        tooltip_header = f'<h3 {header}>Select the level of DLS (Denoised Luma Sharpening)</h3>'
        tooltip_body = f'<p {bodyTop}>Used to set the amount of sharpening in the Denoised Luma Sharpening shader. Higher levels are more sharp.</p><p {bodyBot}>1.00 - Sharpest (More artifacts)<br>0.75 - Sharp<br>0.50 - Medium<br>0.25 - Soft<br>0.00 - Softest (Less artifacts)</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class DLS_Denoise(BaseSetting):
    """
    Class representing the DLS Denoise setting.
    """

    def __init__(self):
        """
        Initializes the DLS Denoise setting.
        """
        title = f'<p>DLS - Denoise&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "1.00", "0.75", "0.50", "0.25", "0.00"]
        tooltip_header = f'<h3 {header}>Select the level of DLS Denoise</h3>'
        tooltip_body = f'<p {bodyTop}>Used to set the amount of denoising in the Denoised Luma Sharpening shader. Higher levels increase the amount of film grain within the image gets sharpened.</p><p {bodyBot}>1.00 - Full<br>0.75 - Most<br>0.50 - Fair<br>0.25 - Default<br>0.00 - Off</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)
