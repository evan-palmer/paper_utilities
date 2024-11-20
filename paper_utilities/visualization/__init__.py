from .color_palette import ColorPalette
from .fonts import load_msttcorefonts_fonts
from .tables import generate_latex_table
from .time_series import plot_time_series

__all__ = [
    "ColorPalette",
    "plot_time_series",
    "load_msttcorefonts_fonts",
    "generate_latex_table",
]
