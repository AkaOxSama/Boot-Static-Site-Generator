import os
import shutil


def copy_static_recursive(source_dir: str, dest_dir: str):
   # Create a directory if none exists
   if not os.path.exists(dest_dir):
      os.mkdir(dest_dir)

   # Creates a list of the contents inside the source directory
   source_contents = os.listdir(source_dir)
   print(f"List of contents in {source_dir}:\n{source_contents}\n")
   for content in source_contents:
      # Creates a path for each content inside the source directory
      source_path = os.path.join(source_dir, content)
      dest_path = os.path.join(dest_dir, content)

      print(f"Filepath for the static file: {source_path}\n")
      # Checks if the content in that path is a file
      if os.path.isfile(source_path):
         # Copies that file from source_dir into des_dir
         shutil.copy(source_path, dest_dir)
         print(f"Source Path: {source_path} is a file...\nCopying contents from {source_path} to {dest_dir}\n")

      # If the content is not a file
      else:
         
         print(f"Source path {source_path} is a directory...\nCreating a destination path:\n{dest_path}\n\n")
         print(f"Creating a directory {content} inside {dest_dir}...\n")
         copy_static_recursive(source_path, dest_path)
         print(f"Copying the contents from {source_path} to {dest_path}")