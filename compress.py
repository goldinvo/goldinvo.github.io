import os
import argparse

def main(source_dir, target_dir):
    for root, dirs, files in os.walk(source_dir):
        # Create corresponding directories in the target directory
        for dir_name in dirs:
            source_subdir = os.path.join(root, dir_name)
            target_subdir = os.path.join(target_dir, os.path.relpath(source_subdir, source_dir))
            os.makedirs(target_subdir, exist_ok=True)

        for file_name in files:
            source_file = os.path.join(root, file_name)
            target_file = os.path.join(target_dir, os.path.relpath(source_file, source_dir))

            if (os.path.exists(target_file)):
                continue

            if '/icons/' in source_file:
                os.system(f"cp {source_file} {target_file}")
            elif any(source_file.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif']):
                os.system(f"magick {source_file} -auto-orient -strip -interlace Plane -resize 1024X1024 -gaussian-blur 0.05 -quality 85% {target_file}")
            elif file_name != '.DS_Store':
                print(f"{source_file} not processed")

    print("Conversion completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process images and directories.')
    parser.add_argument('source_dir', metavar='source_dir', type=str,
                        help='source directory containing images')
    parser.add_argument('target_dir', metavar='target_dir', type=str,
                        help='target directory where processed images will be stored')
    parser.add_argument('--hard', action='store_true',
                        help='overwrite the target directory and process all images again')
    
    args = parser.parse_args()

    source_dir = args.source_dir
    target_dir = args.target_dir
    hard_flag = args.hard

    if hard_flag:
        # If --hard flag is set, remove the target directory and recreate it
        if os.path.exists(target_dir):
            import shutil
            shutil.rmtree(target_dir)
        os.makedirs(target_dir, exist_ok=True)

    main(source_dir, target_dir)
