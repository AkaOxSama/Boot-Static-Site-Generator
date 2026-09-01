import os
import shutil

from website_copy_static import duplicate_static_dir
from website_generate_page import generate_page


script_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(script_dir, "..", "static")
public_dir = os.path.join(script_dir, "..", "public")
content_path = os.path.join(script_dir, "..", "content/index.md")
template_path = os.path.join(script_dir, "..", "template.html")
   
def main():

   duplicate_static_dir(static_dir, public_dir)
   generate_page(content_path, template_path, public_dir)

if __name__ == "__main__":
   main()