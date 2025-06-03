from glob import glob

import matplotlib
import matplotlib.font_manager


def load_msttcorefonts_fonts(
    font_dir: str = "/usr/share/fonts/truetype/msttcorefonts/",
):
    """Load the Microsoft TrueType Core Fonts (msttcorefonts) into matplotlib.

    Microsoft does not permit installation of the Microsoft TrueType Core Fonts
    (msttcorefonts) in Docker containers due to the need to accept a EULA. To address
    this, the fonts should be installed on the host machine and then manually copied into
    the container. This script provides a function to load the fonts into matplotlib
    *after* they have been copied into the container.

    Args:
        font_dir: The full path to the font installation directory. Defaults to
            "/usr/share/fonts/truetype/msttcorefonts/".
    """
    for font in glob(font_dir + "*.ttf"):
        matplotlib.font_manager.fontManager.addfont(font)
