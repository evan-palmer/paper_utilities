import pandas as pd


def _escape(text: str) -> str:
    characters = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        "\\": r"\textbackslash{}",
    }
    return "".join(characters.get(c, c) for c in text)


def _scientific_format(value: float, precision: int) -> str:
    if value == 0:
        return r"0"
    base, exp = f"{value:.{precision}e}".split("e")
    exp = int(exp)
    return f"{base.rstrip('.')}\\text{{e{exp}}}"


def generate_table_from_dataframe(
    data: pd.DataFrame,
    caption: str,
    label: str,
    column_format: str,
    midrules: list[int] | None = None,
    precision: int = 2,
) -> str:
    """Generate a formatted LaTex table from a pandas DataFrame.

    Args:
        data: The pandas DataFrame to use for the table.
        caption: The caption for the table.
        label: The label for the table, used for referencing in LaTeX.
        column_format: The column format for the LaTeX table, e.g., "lccc".
        midrules: A list of row indices where a midrule should be inserted.
        precision: The number of decimal places to use for scientific notation.

    Returns:
        A string containing the LaTeX code for the table.
    """
    columns = data.columns.values.tolist()
    header_row = " & ".join([f"\\textbf{{{col}}}" for col in columns]) + r" \\"

    header = (
        rf"""
\begin{{table*}}[t]
\centering
\rowcolors{{2}}{{gray!20}}{{white}}
\begin{{tabular}}{{{column_format}}}
    \toprule
    {header_row}
    \midrule
    """
        + "\n"
    )

    body = ""
    for i, row in data.iterrows():
        if midrules and i in midrules:
            body += "    " + r"\midrule" + "\n"
            continue
        formatted_row = " & ".join(
            _scientific_format(value, precision)
            if isinstance(value, float)
            else _escape(str(value))
            for value in row
        )
        body += "    " + formatted_row + r" \\" + "\n\n"

    footer = rf"""    \bottomrule
\end{{tabular}}
\caption{{{caption}}}
\label{{tab:{label}}}
\end{{table*}}
"""

    return header + body + footer


def generate_table_from_list(
    data: list,
    columns: list[str],
    caption: str,
    label: str,
    column_format: str,
    midrules: list[int] | None = None,
    precision: int = 2,
) -> str:
    """Generate a formatted LaTex table from a list of data.

    Args:
        data: The list of data to use for the table. The data should be formatted as:
            `[[value1, value2, ...], [value1, value2, ...], ...]`. The data can also
            include tuples/lists for mean and standard deviation, e.g.:
            `[[value1, (mean, std), value3], ...]`.
        columns: The table column names.
        caption: The caption for the table.
        label: The label for the table, used for referencing in LaTeX.
        column_format: The column format for the LaTeX table, e.g., "lccc".
        midrules: A list of row indices where a midrule should be inserted.
        precision: The number of decimal places to use for scientific notation.

    Returns:
        A string containing the LaTeX code for the table.
    """
    if len(columns) != len(data[0]):
        raise ValueError(
            "The number of column names must match the number of columns in the data."
        )
    header_row = " & ".join([f"\\textbf{{{col}}}" for col in columns]) + r" \\"

    header = (
        rf"""
\begin{{table*}}[t]
\centering
\rowcolors{{2}}{{gray!20}}{{white}}
\begin{{tabular}}{{{column_format}}}
    \toprule
    {header_row}
    \midrule
    """
        + "\n"
    )

    body = ""
    for i, row in enumerate(data):
        if midrules and i in midrules:
            body += "    " + r"\midrule" + "\n"

        formatted_row = []
        for col in row:
            if (isinstance(col, tuple) or isinstance(col, list)) and len(col) == 2:
                mean = _scientific_format(col[0], precision)
                std = _scientific_format(col[1], precision)
                formatted_row.append(f"${mean} \\pm {std}$")
            elif isinstance(col, float):
                formatted_row.append(_scientific_format(col, precision))
            else:
                formatted_row.append(_escape(str(col)))
        body += "    " + " & ".join(formatted_row) + r" \\" + "\n\n"

    footer = rf"""    \bottomrule
\end{{tabular}}
\caption{{{caption}}}
\label{{tab:{label}}}
\end{{table*}}
"""

    return header + body + footer
