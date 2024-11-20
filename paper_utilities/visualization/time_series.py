# Copyright 2024, Evan Palmer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import matplotlib.pyplot as plt
import pandas as pd

from paper_utilities.visualization import ColorPalette


def plot_time_series(
    data: pd.DataFrame,
    x: str,
    y: str | list[str],
    ax: plt.Axes,
    xlabel: str = "Time (s)",
    ylabel: str = "Value",
    title: str = "",
    legend_position: str = "upper right",
    linestyle: str = "-",
    color: str | list[str] = ColorPalette.BLACK,
    legend_alpha: float = 0.95,
    linewidth: float = 2,
    fontsize: int = 16,
    title_fontsize: int = 16,
    display_border: bool = False,
    normalize_x: bool = True,
):
    """Plot time-series data.

    Args:
        data: The data to plot, stored in a pandas DataFrame.
        x: The column name of the x-axis data.
        y: The column name of the y-axis data.
        ax: The matplotlib axis to plot on.
        xlabel: The x-axis label. Defaults to "Time (s)".
        ylabel: The y-axis label. Defaults to "Value".
        title: The plot title. Defaults to "".
        legend_position: The position of the legend on the plot. Defaults to "upper
            right".
        linestyle: The time line style for the plot. Defaults to "-". Note that this
            cannot be set per line. There must be a single linestyle for all lines.
        color: The color(s) of the plotted lines. Defaults to ColorPalette.BLACK.
        legend_alpha: The legend alpha value. Defaults to 0.95.
        linewidth: The width of the plotted lines. Defaults to 2.
        fontsize: The size of the font. Defaults to 16.
        title_fontsize: The size of the title font. Defaults to 16.
        display_border: Display a border around the plot. Defaults to False.
        normalize_x: Normalize the x-axis values. Defaults to True. This is useful when
            the x-axis values are timestamps, and you want to plot the data starting at
            zero.
    """
    if normalize_x:
        data[x] = data[x] - data[x].min()

    data.plot(ax=ax, x=x, y=y, color=color, linestyle=linestyle, linewidth=linewidth)

    # Set the labels
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

    # Set the legend position
    ax.legend(loc=legend_position, framealpha=legend_alpha, fontsize=fontsize)

    # Use a GGPlot style
    ax.set_facecolor(ColorPalette.LIGHT_GREY)

    # Set the grid
    ax.grid(True, which="both", color=ColorPalette.WHITE, linestyle="-", linewidth=1.0)
    ax.set_axisbelow(True)

    # Set the title
    ax.set_title(title, fontsize=title_fontsize)

    if not display_border:
        for spine in ax.spines.values():
            spine.set_visible(False)
