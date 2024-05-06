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

class VSYNC(BaseSetting):
    """
    Class representing the VSync setting.
    """

    def __init__(self):
        """
        Initializes the VSync setting.
        """
        title = f'<p>VSync&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "1 Frame", "2 Frames", "Off"]
        tooltip_header = f'<h3 {header}>Select to enable VSync and how many frames</h3>'
        tooltip_body = f'<p {bodyTop}>VSync (Vertical Synchronisation) Vertical Sync (VSync) synchronizes the frame rate of a game with the refresh rate of your monitor to prevent screen tearing. It ensures smoother visuals but may introduce input lag. If frames drop below the VSync level, it can result in performance issues such as stuttering or lower frame rates.</p><p {bodyBot}>1 Frame - Synchronizes the rendering of frames with the display refresh rate, ensuring one frame is displayed per refresh cycle.<br>2 Frames - Synchronizes rendering with the display refresh rate, buffering two frames for reduced tearing and slightly higher latency.</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class VSYNC_D3D9(BaseSetting):
    """
    Class representing the VSync_D3D9 setting.
    """

    def __init__(self):
        """
        Initializes the VSync_D3D9 setting.
        """
        title = f'<p>VSync (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "1 Frame", "2 Frames", "Off"]
        tooltip_header = f'<h3 {header}>Select to enable VSync and how many frames (D3D9 applications only)</h3>'
        tooltip_body = f'<p {bodyTop}>VSync (Vertical Synchronisation) Vertical Sync (VSync) synchronizes the frame rate of a game with the refresh rate of your monitor to prevent screen tearing. It ensures smoother visuals but may introduce input lag. If frames drop below the VSync level, it can result in performance issues such as stuttering or lower frame rates.</p><p {bodyBot}>1 Frame - Synchronizes the rendering of frames with the display refresh rate, ensuring one frame is displayed per refresh cycle.<br>2 Frames - Synchronizes rendering with the display refresh rate, buffering two frames for reduced tearing and slightly higher latency.</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class Frame_Limit(BaseSetting):
    """
    Class representing the Frame_Limit setting.
    """

    def __init__(self):
        """
        Initializes the Frame Limit setting.
        """
        title = f'<p>Frame Limit&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "30", "60", "75", "120", "144", "240", "Off"]
        tooltip_header = f'<h3 {header}>Select the frame limit</h3>'
        tooltip_body = f'<p {bodyTop}>Frame limiting is a technique used to cap the maximum number of frames rendered per second, controlling the rate at which the GPU generates frames for smoother performance.</p><p {bodyBot}>The most common values are:<br>30Hz (30FPS)<br>60Hz (60FPS)<br>75Hz (75FPS)<br>120Hz (120FPS)<br>144Hz (144FPS)<br>240Hz (240FPS)</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)

class Frame_Limit_D3D9(BaseSetting):
    """
    Class representing the Frame_Limit_D3D9 setting.
    """

    def __init__(self):
        """
        Initializes the Frame Limit D3D9 setting.
        """
        title = f'<p>Frame Limit (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "30", "60", "75", "120", "144", "240", "Off"]
        tooltip_header = f'<h3 {header}>Select the frame limit (D3D9 applications only)</h3>'
        tooltip_body = f'<p {bodyTop}>Frame limiting is a technique used to cap the maximum number of frames rendered per second, controlling the rate at which the GPU generates frames for smoother performance.</p><p {bodyBot}>The most common values are:<br>30Hz (30FPS)<br>60Hz (60FPS)<br>75Hz (75FPS)<br>120Hz (120FPS)<br>144Hz (144FPS)<br>240Hz (240FPS)</p>'
        super().__init__(title, options, tooltip_header, tooltip_body)