def generate_latex_table(data):
    if not data or not all(isinstance(row, list) for row in data):
        raise ValueError("Input should be a non-empty list of lists.")

    num_columns = max(len(row) for row in data)

    latex_table = "\\begin{tabular}{|" + "|".join(["c"] * num_columns) + "|}\n"
    latex_table += "\\hline\n"

    for row in data:
        row_str = " & ".join(map(str, row))
        row_str += " \\\\ \\hline\n"
        latex_table += row_str

    latex_table += "\\end{tabular}\n"

    return latex_table


def save_to_file(content, filename="artifacts/table.tex"):
    with open(filename, "w") as file:
        file.write(content)


if __name__ == "__main__":
    table_data = [
        ["Title 1", "Title 2", "Title 3"],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    latex_content = generate_latex_table(table_data)
    save_to_file(latex_content)
