import pandas as pd


def generate_latex_table(data: pd.DataFrame, caption: str, label: str) -> str:
    """Generate a LaTeX table from a DataFrame.

    Args:
        data: The DataFrame to convert to a LaTeX table.
        caption: The caption to include in the table.
        label: The label to include in the table.

    Returns:
        A string containing the LaTeX table.
    """
    latex = data.to_latex(index=False, escape=False)

    lines = latex.splitlines()
    indented_lines = ["    " + lines[0]]
    indented_lines += ["        " + line for line in lines[1:-1]]
    indented_lines.append("    " + lines[-1])
    indented_latex = "\n".join(indented_lines)

    table = (
        "\\begin{table}[!h]\n"
        "    \\centering\n"
        f"{indented_latex}\n"
        "    \\caption{" + caption + "}\n"
        "    \\label{tab:" + label + "}\n"
        "\\end{table}"
    )
    return table
