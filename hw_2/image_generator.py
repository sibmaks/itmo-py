import subprocess

from latex_table_generator.latex_table_generator import generate_latex_table


def generate_image(path):
    if not path or not isinstance(path, str):
        raise ValueError("Input should be a non-empty string")

    return "\\includegraphics{%s}" % path


def create_latex_with_image(content):
    if not content or not isinstance(content, str):
        raise ValueError("Content should be a non-empty string")
    return """
\\documentclass{article}
\\usepackage{graphicx}
\\graphicspath{ {./artifacts/} }

\\begin{document}
%s
\\end{document}
""" % content


def save_to_file(content, filename="artifacts/input.tex"):
    with open(filename, "w") as file:
        file.write(content)


def render_latex(path):
    return subprocess.run(['pdflatex', '-output-directory', 'artifacts', path])


if __name__ == "__main__":
    table_data = [
        ["Title 1", "Title 2", "Title 3"],
        [1, 2, 3],
        [4, generate_image('img.png'), 6],
        [7, 8, 9]
    ]

    latex_content = generate_latex_table(table_data)
    latex_doc = create_latex_with_image(latex_content)
    image_latex_path = "artifacts/image.tex"
    save_to_file(latex_doc, image_latex_path)

    render_latex(image_latex_path)
