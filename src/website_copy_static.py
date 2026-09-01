import os
import shutil

def duplicate_static_dir(scr_path: str, dst_path: str):
   # Checks if the directory 'public' exists and deletes it and all its contents
   if os.path.exists(dst_path):
      print(f"Filepath:    {dst_path}     Exists, deleting the directory...")
      shutil.rmtree(dst_path)

   # Creates a 'public' clean directory
   os.mkdir(dst_path)
   print(f"Created directory: {dst_path}\n\n")

   # Calls the copy function
   copy_static_recursive(scr_path, dst_path)


def copy_static_recursive(source_dir: str, dest_dir: str):
   # Creates a list of the contents inside the source directory
   source_contents = os.listdir(source_dir)
   print(f"List of contents in {source_dir}:\n{source_contents}\n")
   for content in source_contents:
      # Creates a path for each content inside the source directory
      source_path = os.path.join(source_dir, content)
      print(f"Filepath for the static file: {source_path}\n")
      # Checks if the content in that path is a file
      if os.path.isfile(source_path):
         # Copies that file from source_dir into des_dir
         shutil.copy(source_path, dest_dir)
         print(f"Source Path: {source_path} is a file...\nCopying contents from {source_path} to {dest_dir}\n")

      # If the content is not a file
      else:
         dest_path = os.path.join(dest_dir, content)
         print(f"Source path {source_path} is a directory...\nCreating a destination path:\n{dest_path}\n\n")
         print(f"Creating a directory {content} inside {dest_dir}...\n")
         os.mkdir(dest_path)
         copy_static_recursive(source_path, dest_path)
         print(f"Copying the contents from {source_path} to {dest_path}")