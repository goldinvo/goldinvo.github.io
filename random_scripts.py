import os
import yaml

# Reorders frontmatter dict --> dict with the correct insertion order.
def reorder_frontmatter(frontmatter):
    SCHEMA_ORDER = [
        "title",
        "description",
        "grade",        
    ]
    
    ordered = {} # maintains insertion order
    for key in SCHEMA_ORDER:
        if key in frontmatter:
            ordered[key] = frontmatter[key]
    # Add leftover keys at the end
    for key in frontmatter:
        if key not in SCHEMA_ORDER:
            ordered[key] = frontmatter[key]
    return ordered

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines or lines[0].strip() != "---":
        print(f"Skipping {filepath}: No front matter")
        return

    # Find end of front matter
    try:
        end_idx = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        print(f"Skipping {filepath}: No closing --- for front matter")
        return

    # Parse YAML front matter
    frontmatter = yaml.safe_load("".join(lines[1:end_idx]))
    content = "".join(lines[end_idx + 1:])

    ### Modify front matter here ###
    frontmatter = reorder_frontmatter(frontmatter)
    if 'index' not in filepath:
        if frontmatter.get('grade') == 'E' or frontmatter.get('grade') == 'S':
            frontmatter["updatedDate"] = '2025-07-09'
        else:
            frontmatter["updatedDate"] = '2000-01-01'
    #################################

    # Write updated content back
    with open(filepath, "w", encoding="utf-8") as file:
        file.write("---\n")
        yaml.dump(frontmatter, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
        file.write("---\n")
        file.write(content)

def main():
    root_dir = "/Users/goldinbaokimvo/projects/blog/src/content/cooking"
    
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(dirpath, filename)
                process_file(filepath)

if __name__ == "__main__":
    main()