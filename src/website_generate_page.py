from website_extract_title import extract_title
from blocks_markdown import markdown_to_html_node

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