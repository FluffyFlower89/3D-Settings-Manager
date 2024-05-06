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

class SMAA(BaseSetting):
    """
    Class representing the SMAA (Subpixel Morphological Anti-Aliasing) setting.
    """

    def __init__(self):
        """
        Initializes the SMAA setting.
        """
        title = f'<p>SMAA - Subpixel Morphological Anti-Aliasing&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Enabled", "Disabled"]
        tooltip_header = f'<h3 {header}>Select whether to enable SMAA:</h3>'
        tooltip_body = f'<p {bodyTop}>Subpixel Morphological Anti-Aliasing. This is a graphics rendering technique used to smooth jagged edges and reduce aliasing, it is more performance heavy than FXAA</p><p {bodyBot}>Enabled - Turns on FXAA.<br>Disabled - Turns off FXAA.</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class SMAA_Edge_Detection(BaseSetting):
    """
    Class representing the SMAA Edge Detection setting.
    """

    def __init__(self):
        """
        Initializes the SMAA Edge Detection setting.
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Edge Detection&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Luma", "Color"]
        tooltip_header = f'<h3 {header}>Changes the edge detection shader.</h3>'
        tooltip_body = f'<p {bodyBot}>Luma - Default<br>Color - Catches more edges, but is more expensive</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class SMAA_Threshold(BaseSetting):
    """
    Class representing the SMAA Threshold setting.
    """

    def __init__(self):
        """
        Initializes the SMAA Threshold setting.
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Threshold&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Options...", "Highest Quality", "Quality", "Balanced", "Low Quality", "Lowest Quality"]
        tooltip_header = f'<h3 {header}>Specifies the threshold or sensitivity to edges</h3>'
        tooltip_body = f'<p {bodyTop}>Lowering this value you will be able to detect more edges at the expense of performance.<br>Higher values increase performance, at the expense of image quality.</p><p {bodyBot}>Highest Quality - (0.05) Overkill<br>Quality - (0.10)<br>Balanced - (0.25)<br>Low Quality - (0.40)<br>Lowest Quality - (0.50)</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class SMAA_Search_Steps(BaseSetting):
    """
    Class representing the SMAA Max Search Steps setting.
    """

    def __init__(self):
        """
        Initializes the SMAA Max Search Steps setting.
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Max Search Steps&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Options...", "x32", "x16", "x8", "x4", "x2"]
        tooltip_header = f'<h3 {header}>Specifies the maximum steps performed in the horizontal/vertical pattern searches</h3>'
        tooltip_body = f'<p {bodyTop}>Higher values give higher image quality, at the expense of performance.<br>Lower values give higher performance, at the expense of image quality</p><p {bodyBot}>x32 - Highest Quality<br>x16 - High Quality<br>x8 - Balanced<br>x4 - Low Quality<br>x2 - Lowest Quality</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class SMAA_Search_Steps_Diagonal(BaseSetting):
    """
    Class representing the SMAA Max Diagonal Search Steps setting.
    """

    def __init__(self):
        """
        Initializes the SMAA Max Diagonal Search Steps setting.
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Max Diagonal Search Steps&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Options...", "x16", "x8", "x4", "x2", "x0"]
        tooltip_header = f'<h3 {header}>Specifies the maximum steps performed in the diagonal pattern searches</h3>'
        tooltip_body = f'<p {bodyTop}>Higher values give higher image quality, at the expense of performance.<br>Lower values give higher performance, at the expense of image quality</p><p {bodyBot}>x16 - Highest Quality<br>x8 - High Quality<br>x4 - Balanced<br>x2 - Low Quality<br>x0 - Lowest Quality</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class SMAA_Corner_Rounding(BaseSetting):
    """
    Class representing the SMAA Corner Rounding setting.
    """

    def __init__(self):
        """
        Initializes the SMAA Corner Rounding setting.
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Corner Rounding&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Options...", "100", "75", "50", "25", "0"]
        tooltip_header = f'<h3 {header}>Specifies how much sharp corners will be rounded</h3>'
        tooltip_body = f'<p {bodyTop}>Higher values round corners more.<br>Lower values round corners less (Adjust to your preference)</p><p {bodyBot}>100 - Highest Quality<br>75 - High Quality<br>50 - Balanced<br>25 - Low Quality<br>0 - Lowest Quality</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)
