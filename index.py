import os
import json

# Create a directory for the digital library
library_dir = os.path.join(os.getcwd(), "library")
os.mkdir(library_dir)

# Create a file to store the library metadata
metadata_file = os.path.join(library_dir, "metadata.json")
with open(metadata_file, "w") as f:
    json.dump({}, f)

# Create a function to add a book to the library
def add_book(title, author, file_path):
    """Adds a book to the digital library.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        file_path (str): The path to the book file.
    """

    # Get the library metadata
    with open(metadata_file, "r") as f:
        metadata = json.load(f)

    # Add the book to the metadata
    metadata["books"].append({
        "title": title,
        "author": author,
        "file_path": file_path,
    })

    # Save the library metadata
    with open(metadata_file, "w") as f:
        json.dump(metadata, f)

# Add a few books to the library
add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "hitchhikers_guide.pdf")
add_book("The Lord of the Rings", "J.R.R. Tolkien", "lord_of_the_rings.pdf")
add_book("The Great Gatsby", "F. Scott Fitzgerald", "great_gatsby.pdf")

# Print the library metadata
with open(metadata_file, "r") as f:
    metadata = json.load(f)
    print(metadata)
