import os
import yaml

# Define the schema order
SCHEMA_ORDER = [
    "title",
    "description",
    "pubDate",
    "updatedDate",
    "type",
    "featuredImage",
    "images",
    "tags",
    "featured"
]

# Reorder frontmatter based on schema
def reorder_frontmatter(frontmatter):
    ordered = {}
    for key in SCHEMA_ORDER:
        if key in frontmatter:
            ordered[key] = frontmatter[key]
    # Add remaining keys not in the schema order
    for key in frontmatter:
        if key not in SCHEMA_ORDER:
            ordered[key] = frontmatter[key]
    return ordered

# Process files in the directory
def process_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mdx") or filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                lines = file.readlines()
            
            # Extract and process frontmatter
            if lines[0].strip() == "---":
                end_idx = lines[1:].index("---\n") + 1
                frontmatter = yaml.safe_load("".join(lines[1:end_idx]))
                content = "".join(lines[end_idx+1:])

                # Reorder frontmatter
                frontmatter = reorder_frontmatter(frontmatter)

                # Overwrite original file with .md extension
                new_filename = filename.replace(".mdx", ".md")
                new_filepath = os.path.join(directory, new_filename)
                with open(new_filepath, "w", encoding="utf-8") as file:
                    file.write("---\n")
                    yaml.dump(frontmatter, file, default_flow_style=False, sort_keys=False)
                    file.write("---\n")
                    file.write(content)
                
                # Remove the original .mdx file if necessary
                if filename.endswith(".mdx"):
                    os.remove(filepath)

# Replace with the directory containing your .mdx/.md files
directory = "/Users/goldinbaokimvo/projects/blog/src/content/blog"
process_files(directory)
