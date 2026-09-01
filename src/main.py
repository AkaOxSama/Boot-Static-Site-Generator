import os
import shutil

from website_copy_static import duplicate_static_dir
from website_generate_page import generate_page



script_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(script_dir, "..", "static")
public_dir = os.path.join(script_dir, "..", "public")
content_dir = os.path.join(script_dir, "..", "content")
template_path = os.path.join(script_dir, "..", "template.html")


def main():
   print(f"Generating a clean public directory in: {public_dir}...\n")
   duplicate_static_dir(static_dir, public_dir)
   print("Creating contents for the webpage...")
   
   generate_page(os.path.join(content_dir, "index.md"), template_path, os.path.join(public_dir, "index.html"))

if __name__ == "__main__":
   main()