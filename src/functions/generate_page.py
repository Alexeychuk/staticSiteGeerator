import os

from .extract_title import extract_title
from .markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    content = ""
    template = ""

    with open(from_path, "r", encoding="utf-8") as file:
        content = file.read()

    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()
    markdown = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    prepared_template = template.replace("{{ Title }}", title)
    prepared_template = prepared_template.replace("{{ Content }}", markdown)

    prepared_template = prepared_template.replace('href="/', f'href="{basepath}')
    prepared_template = prepared_template.replace('src="/', f'src="{basepath}')

    if not os.path.isdir(dest_path):
        os.makedirs(dest_path)

    with open(os.path.join(dest_path, "index.html"), "w") as file:
        file.write(prepared_template)
