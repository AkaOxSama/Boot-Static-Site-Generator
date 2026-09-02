import os
import pathlib

from website_extract_title import extract_title
from blocks_markdown import markdown_to_html_node


# Webpage generator
def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the index.md file and store it in a variable
    with open(from_path) as md_source:
        md_text = md_source.read()

    # Convert the md_text into html_text
    html_node = markdown_to_html_node(md_text)
    html_text = html_node.to_html()

    # Extract the title from the md_file
    title = extract_title(md_text)

    # read the template.html file
    with open(template_path) as html_template:
        html_body = html_template.read()
        # create a html text with the title and content replaced with the apropiate variables
        html_body = html_body.replace("{{ Title }}", title).replace("{{ Content }}", html_text)

    # Create a file index.html in the public directory
    
    open(dest_path, "a")
    with open(dest_path, "w") as f:
        f.write(html_body)


# Recursive webpage generator
def generate_pages_recursive(dir_path_content: list[str], template_path: str, des_dir_path: str):
    des_p = pathlib.Path(des_dir_path)
    
    for content in dir_path_content:
        cont_p = pathlib.Path(content)

        if cont_p.is_file() and cont_p.suffix == ".md":
            dest_file = des_p / f"{cont_p.stem}.html"
            print(f"Generating html file at: {des_p.absolute()}\n")
            generate_page(cont_p.absolute(), template_path, dest_file.absolute())

        elif cont_p.is_dir():
            new_des_path = des_p / content
            new_des_path.mkdir(parents=True, exist_ok=True)

            print(f"Created directory at: {new_des_path.absolute()}\n")

            old_dir = os.getcwd()
            os.chdir(cont_p.absolute())

            generate_pages_recursive(
                os.listdir(),
                template_path, 
                new_des_path.absolute()
            )

            os.chdir(old_dir)

os.chdir("/home/akaox/BootProj/Boot-Static-Site-Generator/content")

generate_pages_recursive(os.listdir(), "/home/akaox/BootProj/Boot-Static-Site-Generator/template.html", "/home/akaox/BootProj/Boot-Static-Site-Generator/public")