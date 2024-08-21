import os
import yaml

# Define the directory containing the files to process
root_dir = '/Users/goldinbaokimvo/projects/new-blog/src/content/cooking'

# Function to fix front matter
def fix_front_matter(content):
    # Split content into front matter and the rest
    if content.startswith('---'):
        _, front_matter, body = content.split('---', 2)
        front_matter = yaml.safe_load(front_matter.strip())
        
        # Create a new front matter with only the required fields
        new_front_matter = {
            'title': front_matter.get('title', ''),
            'grade': front_matter.get('grade', 'S')
        }
        
        # Add optional fields only if they exist
        if 'description' in front_matter:
            new_front_matter['description'] = front_matter['description']
        if 'custom_folder_order' in front_matter:
            new_front_matter['customFolderOrder'] = front_matter['custom_folder_order']
        if 'images' in front_matter:
            new_front_matter['images'] = front_matter['images']
        
        # Convert the updated front matter back to string
        new_front_matter_str = yaml.dump(new_front_matter, default_flow_style=False, allow_unicode=True).strip()
        
        # Combine the updated front matter with the body
        new_content = f'---\n{new_front_matter_str}\n---\n{body.strip()}'
        return new_content
    return content

# Walk through all files in the directory and subdirectories
for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        
        # Only process markdown files
        if file_path.endswith('.md'):
            with open(file_path, 'r') as file:
                content = file.read()
            
            # Fix the front matter
            new_content = fix_front_matter(content)
            
            # Save the file with the new content
            with open(file_path, 'w') as file:
                file.write(new_content)
