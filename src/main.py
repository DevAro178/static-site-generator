import os, sys
import shutil
from textnode import TextNode,TextType
from generator import generate_pages_recursive

def copy_static(src, dst):
    # Delete destination if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)

    # Recreate destination directory
    os.mkdir(dst)

    # Iterate through source contents
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Copying directory: {src_path} -> {dst_path}")
            copy_static(src_path, dst_path)


def main():
    basepath = "/"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    # Build into docs instead of public
    output_dir = "docs"
    
    copy_static("static", output_dir)

    generate_pages_recursive(
        "content",
        "template.html",
        output_dir,
        basepath
    )


if __name__ == "__main__":
    main()
