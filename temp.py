import os
import yaml
import re

# Define the directory containing your .md files
directory = '/Users/goldinbaokimvo/projects/blog/src/content/blog'

# Function to extract pubDate from YAML front matter
def get_pub_date(md_content):
    try:
        # Match the YAML front matter
        yaml_match = re.match(r'^---\n(.*?)\n---', md_content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml.safe_load(yaml_match.group(1))
            return yaml_content.get('pubDate', None)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
    return None

# Process each .md file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.md'):
        file_path = os.path.join(directory, filename)

        # Read the file contents
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Extract the pubDate
        pub_date = get_pub_date(content)
        
        # If pubDate is found, rename the file and convert extension to .mdx
        if pub_date:
            # Format the new file name
            new_filename = f"{pub_date}-{filename.replace('.md', '.mdx')}"
            new_file_path = os.path.join(directory, new_filename)

            # Write the content to the new .mdx file
            with open(new_file_path, 'w', encoding='utf-8') as new_file:
                new_file.write(content)

            # Optionally, remove the old .md file
            os.remove(file_path)

            print(f"Converted and renamed: {filename} -> {new_filename}")

print("Conversion completed.")