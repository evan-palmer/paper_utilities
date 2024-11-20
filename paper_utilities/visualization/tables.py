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
