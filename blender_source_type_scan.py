import os


def scan_file_types(directory):
    file_types = set()

    # Iterate through the files and directories in the given directory
    for root, dirs, files in os.walk(directory):

        # Iterate through the files
        for file in files:

            # Get the file extension
            file_ext = os.path.splitext(file)[1]

            # Add the file type to the set
            file_types.add(file_ext)

    return file_types


if __name__ == "__main__":
    start_directory = "G:\\ClayTree\\BlenderSource"
    unique_file_types = scan_file_types(start_directory)
    print(f"Unique file types: {unique_file_types}")