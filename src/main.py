import os
import sys
import shutil

from website_copy_static import copy_static_recursive
from gencontent import generate_pages_recursive

static_path = "./static"
public_path = "./public"
content_path = "./content"
template_path = "./template.html"
docs_path = "./docs"
default_basepath = "/"


def main():
   basepath = default_basepath
   if len(sys.argv) > 1:
      basepath = sys.argv[1]

   print("Deleting docs directory...")
   if os.path.exists(docs_path):
      shutil.rmtree(docs_path)

   print(f"Generating a clean docs directory in: {docs_path}...\n")
   copy_static_recursive(static_path, docs_path)
   print("Creating contents for the webpage...\n")
   print("\n")
   
   print("Creating web pages...\n")
   generate_pages_recursive(content_path, template_path, docs_path, basepath)
   

   


main()