# Doginals Hash Canvas Encoder for New Collections and mints

- The Doginals Hash Canvas Encoder script encodes hidden messages into images using the Least Significant Bit (LSB) method provided by the stegano library.

## Prerequisites

Make sure you have the following dependencies installed:

- [stegano](https://pypi.org/project/stegano/)
- [Pillow](https://pypi.org/project/Pillow/)

You can install them using the following commands:

`pip install stegano`

`pip install Pillow`

## Usage

-Clone the Repository:

git clone https://github.com/GreatApe42069/Doginals_Hash_Canvas_Creator.git
cd DoginalsHashCanvasCreator

## Prepare JSON File:

-Create a JSON file (((encoded_messages.json))) containing image paths and corresponding hidden messages which "YOU INPUT IN THIS json". Ensure the paths are correctly formatted and double-check for any escaping issues.
***Enter file path and Hidden message inside the ((`encoded_messages.json`)) inside the Main folder not in dist folder , in the Main folder. Make sure to use double    \\  if you use  \  in file path input you will get, Error loading JSON file: Invalid \escape: line 3 column 26 (char 33)***

## Example:

[
    {
        "image_path": "path/to/image1.png",
        "hidden_message": "This is a secret message for image 1"
    },
    {
        "image_path": "path/to/image2.png",
        "hidden_message": "Another secret message for image 2"
    }
]


## Run the Encoder:

-Execute the encoder script to encode the hidden messages into the images.

`python Hidden_Encoder.py`

*The encoded images will be saved in the C:/DoginalsHashCanvasCreator/encoded_images directory.*


## Notes:

The script uses the '|||' delimiter to separate the hidden message during encoding. Ensure the same delimiter is used for decoding.

Check the console output for success messages or error details.

Ensure that the 'C:/DoginalsHashCanvasCreator/encoded_images' directory exists before running the script.

### Issues and Support:

For any issues or further assistance, feel free to open an issue on the repository.

## License
This script is licensed under the MIT License.

Feel free to modify and adapt the script to suit your needs.

# Happy encoding!

