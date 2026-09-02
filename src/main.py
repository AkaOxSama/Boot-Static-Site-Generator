import os
import shutil
import pathlib

from website_copy_static import duplicate_static_dir
from website_generate_page import generate_pages_recursive



script_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(script_dir, "..", "static")
public_dir = os.path.join(script_dir, "..", "public")
content_dir = os.path.join(script_dir, "..", "content")
template_path = os.path.join(script_dir, "..", "template.html")


def main():
   print(f"Generating a clean public directory in: {public_dir}...\n")
   duplicate_static_dir(static_dir, public_dir)
   print("Creating contents for the webpage...\n")
   print("\n")
   
   dir_contents = os.listdir(content_dir)
   print("Creating web pages...\n")
   generate_pages_recursive(dir_contents, template_path, public_dir)
   

   

if __name__ == "__main__":
   main()