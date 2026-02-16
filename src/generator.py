import os
from blocktype import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise Exception("No h1 header found in markdown")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    content_html = html_node.to_html()

    title = extract_title(markdown)

    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", content_html)

    # Rewrite absolute URLs with basepath
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(final_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(content_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(
                content_path,
                template_path,
                dest_path,
                basepath,
            )

        elif os.path.isfile(content_path) and entry.endswith(".md"):
            html_filename = entry.replace(".md", ".html")
            final_dest_path = os.path.join(dest_dir_path, html_filename)

            generate_page(
                content_path,
                template_path,
                final_dest_path,
                basepath,
            )
