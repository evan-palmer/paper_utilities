import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from paper_utilities.visualization import ColorPalette


def plot_time_series_from_dataframe(
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


def plot_time_series_from_array(
    x: np.ndarray,
    y: np.ndarray,
    ax: plt.Axes,
    axis: int = 0,
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
    legend_label: str | list[str] | None = None,
    show_legend: bool = True,
):
    """Plot time-series data.

    Args:
        x: The x-axis data to plot.
        y: The y-axis data to plot. This can be either a 1D or 2D array. If it is a 2D
            array, use the axis parameter to specify which axis to plot over.
        ax: The matplotlib axis to plot on.
        axis: The axis to plot over if y is a 2D array. Defaults to 0.
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
        legend_label: The label(s) for the legend. Defaults to None. If y is a 2D array,
            this should be a list of labels for each line in the plot. If y is a 1D
            array, this should be a single label for the plot.
        show_legend: Show the legend on the plot. Defaults to True.
    """
    if normalize_x:
        x = x - x.min()

    if len(y.shape) > 1:
        if isinstance(color, str):
            for i in range(y.shape[axis]):
                ys = y.take(i, axis)
                ax.plot(
                    x,
                    ys,
                    color=color,
                    linestyle=linestyle,
                    linewidth=linewidth,
                    label=legend_label[i] if isinstance(legend_label, list) else None,
                )
        else:
            for i in range(y.shape[axis]):
                ys = y.take(i, axis)
                ax.plot(
                    x,
                    ys,
                    color=color[i],
                    linestyle=linestyle,
                    linewidth=linewidth,
                    label=legend_label[i] if isinstance(legend_label, list) else None,
                )
    else:
        if isinstance(color, str):
            ax.plot(
                x,
                y,
                color=color,
                linestyle=linestyle,
                linewidth=linewidth,
                label=legend_label,
            )
        else:
            ax.plot(
                x,
                y,
                color=color[0],
                linestyle=linestyle,
                linewidth=linewidth,
                label=legend_label,
            )

    # Set the labels
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

    # Set the legend position
    if show_legend:
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
