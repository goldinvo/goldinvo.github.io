import os
import shutil

def flatten_directory_structure(base_dir):
    # Walk through the directory tree
    for root, dirs, files in os.walk(base_dir, topdown=False):
        for name in files:
            # Generate the new file path with hyphens
            relative_path = os.path.relpath(os.path.join(root, name), base_dir)
            new_name = relative_path.replace(os.sep, '-')
            new_path = os.path.join(base_dir, new_name)

            # Move the file to the new flattened path
            shutil.move(os.path.join(root, name), new_path)

        # After moving all files, remove the now empty directories
        for name in dirs:
            dir_path = os.path.join(root, name)
            if not os.listdir(dir_path):  # Check if the directory is empty
                os.rmdir(dir_path)

if __name__ == "__main__":
    base_directory = '/Users/goldinbaokimvo/projects/goldinvo.github.io/src/assets'
    flatten_directory_structure(base_directory)

# import os
# import yaml

# # Define the directory containing the files to process
# root_dir = '/Users/goldinbaokimvo/projects/goldinvo.github.io/src/content'

# # Function to fix front matter
# def fix_front_matter(content):
#     # Split content into front matter and the rest
#     if content.startswith('---'):
#         _, front_matter, body = content.split('---', 2)
#         front_matter = yaml.safe_load(front_matter.strip())
        
#         if 'images' in front_matter:
#             front_matter['images'] = ['@assets/'+path.strip('/').replace('/', '-') for path in front_matter['images']]
#         if 'featuredImage' in front_matter:
#             front_matter['featuredImage'] = '@assets/'+front_matter['featuredImage'].strip('/').replace('/', '-')

#         # Convert the updated front matter back to string
#         new_front_matter_str = yaml.dump(front_matter, default_flow_style=False, allow_unicode=True).strip()
        
#         # Combine the updated front matter with the body
#         new_content = f'---\n{new_front_matter_str}\n---\n{body.strip()}'
#         return new_content
#     return content

# # Walk through all files in the directory and subdirectories
# for dirpath, _, filenames in os.walk(root_dir):
#     for filename in filenames:
#         file_path = os.path.join(dirpath, filename)
        
#         # Only process markdown files
#         if file_path.endswith('.md'):
#             with open(file_path, 'r') as file:
#                 content = file.read()
            
#             # Fix the front matter
#             new_content = fix_front_matter(content)
            
#             # Save the file with the new content
#             with open(file_path, 'w') as file:
#                 file.write(new_content)
