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

class Anistropic_Filtering(BaseSetting):
    """
    Class representing the Anistropic_Filtering setting.
    """

    def __init__(self):
        """
        Initializes the Anistropic Filtering setting.
        """
        title = f'<p>Anistropic Filtering&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "x16", "x8", "x4", "x2", "x1", "0"]
        tooltip_header = f'<h3 {header}>Select the level of Anistropic Filtering:</h3>'
        tooltip_body = f'<p {bodyTop}>Anisotropic filtering is a texture filtering technique that enhances the clarity of distant textures in 3D rendering by improving the sharpness of textures viewed at oblique angles, with higher levels providing sharper textures but requiring more resources compared to lower levels.</p><p {bodyBot}>x16 Samples - High Quality<br>x8 Samples - Quality<br>x4 Samples - Balanced<br>x2 Samples - Performance<br>x1 Sample - High Performance<br>x0 Samples - Off</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class Anistropic_Filtering_D3D9(BaseSetting):
    """
    Class representing the Anistropic_Filtering_D3D9 setting.
    """

    def __init__(self):
        """
        Initializes the Anistropic Filtering D3D9 setting.
        """
        title = f'<p>Anistropic Filtering (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "x16", "x8", "x4", "x2", "x1", "0"]
        tooltip_header = f'<h3 {header}>(D3D9 applications only) Select the level of Anistropic Filtering:</h3>'
        tooltip_body = f'<p {bodyTop}>Anisotropic filtering is a texture filtering technique that enhances the clarity of distant textures in 3D rendering by improving the sharpness of textures viewed at oblique angles, with higher levels providing sharper textures but requiring more resources compared to lower levels.</p><p {bodyBot}>x16 Samples - High Quality<br>x8 Samples - Quality<br>x4 Samples - Balanced<br>x2 Samples - Performance<br>x1 Sample - High Performance<br>x0 Samples - Off</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class LOD_Bias(BaseSetting):
    """
    Class representing the LOD_Bias setting.
    """

    def __init__(self):
        """
        Initializes the LOD Bias setting.
        """
        title = f'<p>LOD Bias&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "-2", "-1", "0", "0.5", "1"]
        tooltip_header = f'<h3 {header}>Select the level of LOD Bias:</h3>'
        tooltip_body = f'<p {bodyTop}>LOD bias, or Level of Detail bias, is a rendering technique used to control the level of detail of textures based on their distance from the viewer. Lower or negative values of LOD bias result in higher texture detail for distant objects, while higher or positive values reduce texture detail to improve performance.</p><p {bodyBot}>-2 - Highest Quality<br>-1 - High Quality<br>0 - Balanced<br>0.5 - Low Quality<br>1 - Lowest Quality</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class LOD_Bias_D3D9(BaseSetting):
    """
    Class representing the LOD_Bias_D3D9 setting.
    """

    def __init__(self):
        """
        Initializes the LOD Bias D3D9 setting.
        """
        title = f'<p>LOD Bias (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "-2", "-1", "0", "0.5", "1"]
        tooltip_header = f'<h3 {header}>(D3D9 applications only) Select the level of LOD Bias:</h3>'
        tooltip_body = f'<p {bodyTop}>LOD bias, or Level of Detail bias, is a rendering technique used to control the level of detail of textures based on their distance from the viewer. Lower or negative values of LOD bias result in higher texture detail for distant objects, while higher or positive values reduce texture detail to improve performance.</p><p {bodyBot}>-2 - Highest Quality<br>-1 - High Quality<br>0 - Balanced<br>0.5 - Low Quality<br>1 - Lowest Quality</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class Clamp_Negative_LOD(BaseSetting):
    """
    Class representing the Clamp_Negative_LOD setting.
    """

    def __init__(self):
        """
        Initializes the Clamp Negative LOD setting.
        """
        title = f'<p>Clamp Negative LOD Bias&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Enabled", "Disabled"]
        tooltip_header = f'<h3 {header}>Select whether to enable negative LOD bias clamping</h3>'
        tooltip_body = f'<p {bodyTop}>Clamps the negative values of LOD bias to 0, helps in games that use a high negative LOD bias by default.</p><p {bodyBot}></p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class Clamp_Negative_LOD_D3D9(BaseSetting):
    """
    Class representing the Clamp_Negative_LOD_D3D9 setting.
    """

    def __init__(self):
        """
        Initializes the Clamp Negative LOD D3D9 setting.
        """
        title = f'<p>Clamp Negative LOD Bias (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Enabled", "Disabled"]
        tooltip_header = f'<h3 {header}>(D3D9 applications only) Select whether to enable negative LOD bias clamping</h3>'
        tooltip_body = f'<p {bodyTop}>Clamps the negative values of LOD bias to 0, helps in games that use a high negative LOD bias by default.</p><p {bodyBot}></p>'
        super().__init__(title, options, tooltip_header, tooltip_body)