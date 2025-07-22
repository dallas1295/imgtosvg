import argparse
from .converter import convert_image


def main():
    """
    Main function for CLI
    """

    parser = argparse.ArgumentParser(description="Convert any image to SVG format")
    parser.add_argument("input_path", type=str, help="The image to be converted's path")
    parser.add_argument(
        "output_file", type=str, help="The desired name for the converted image"
    )

    args = parser.parse_args()

    convert_image(args.input_path, args.output_file)


if __name__ == "__main__":
    main()
