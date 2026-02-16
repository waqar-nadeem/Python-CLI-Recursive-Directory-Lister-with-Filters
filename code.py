import os
import argparse

def list_files(directory, extension=None):
    for root, _, files in os.walk(directory):
        for file in files:
            if extension is None or file.endswith(extension):
                print(os.path.join(root, file))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--ext", help="Filter by file extension", default=None)
    args = parser.parse_args()
    list_files(args.directory, args.ext)
