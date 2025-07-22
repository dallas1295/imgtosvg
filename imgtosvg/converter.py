import vtracer
from pathlib import Path


def convert_image(input_path, output_name):
    """
    Converts regular image file to an SVG
    """

    # Take the input value and ensure it exists
    input_file = Path(input_path)
    if not input_file.exists() and input_file.is_file():
        print(f"Error: The provided path is not a valid file")
        return

    # Create the file path for converted SVG
    user_documents = Path.home() / "Documents"
    output_filename = output_name + ".svg"
    final_path = user_documents / output_filename

    print(f"Converting {input_path} to {output_filename}")
    vtracer.convert_image_to_svg_py(str(input_file), str(final_path))

    print(
        f"{input_file} has been converter as {output_filename} in the Documents directory)"
    )
