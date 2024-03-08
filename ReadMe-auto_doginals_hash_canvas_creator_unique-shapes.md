# TX Hash Unique Shapes Image Generator

The Doginals Auto Unique Shape Canvas Creator, creates images based on transaction hashes and saves them in the 'generated_images' directory. Each image is created dynamically, with colors, and containing randomly placed rectangles and ellipses. The colors of these shapes are determined by the SHA-256 hash of the transaction. derived from a cryptographic hash function (e.g., SHA-256) to generate a unique hash or binary representation of specific hash transaction id's. The generated images are saved in the PNG format, with the encoded additional information added through steganography. 

## Prerequisites

Python 3.x

Pillow library 

Stegano


# Install dependencies:

Ensure you have the following dependencies installed:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [PIL](https://pillow.readthedocs.io/) (Python Imaging Library)
- [stegano](https://github.com/ouanixi/stegano) (Steganography library)

You can install the required Python packages using the following command:

`pip install pillow stegano`

or

`pip install stegano==0.9.8`


or

`pip install --upgrade stegano`


if you get an error open the administrator command prompt, you now will run these installation commands:


`python -m pip install --upgrade pip
pip install --force-reinstall stegano`


If you encounter any further permission issues, you can try adding the --user option to the pip install command. For example:

`pip install --force-reinstall --user stegano`


Install needed requirements:

`pip install -r requirements.txt`
 

## Usage

Clone the Repository:

git clone https://github.com/GreatApe42069/Doginals_Hash_Canvas_Creator.git
cd DoginalsHashCanvasCreator

## Run the Script:

`python auto_doginals_hash_canvas_creator_unique_shapes.py`

This will generate an image based on a transaction hash and save it in the 'hash-map_generated_images' directory.

## Implementation

The script uses the Pillow library for image manipulation. It dynamically creates and saves images by randomly placing rectangles and ellipses on a white or black canvas depending on how you edit paremeters. The seed for the random number generator is derived from the transaction hash, ensuring reproducibility for a given hash, then it encodes tx id and hidden message within.

## Functions

`create hash-map_generated_images_directory()`
Creates the 'hash-map_generated_images' directory if it doesn't exist.


`render_image(transaction_hash)`
Generates a unique image based on the transaction hash. It creates a black canvas and draws random shapes (rectangles or ellipses) with colors, shapes, and positon determined by the hash. The final image is encoded and saved in the 'hash-map_generated_images' directory.

## Notes:

The number of possibilities for colors and patterns in your script depends on the random choices made during the drawing process. Let's break down the possibilities.

### Size and Position:

The position (x1, y1, x2, y2) of each shape is randomly determined within the bounds of the image (500x500 pixels).
The width (x2 - x1) and height (y2 - y1) of each shape are randomly determined within specific ranges (33 to 69 and 22 to 77, respectively).

- `for _ in range(77)`

this parameter runs an image creation loop it runs 77 times, and for each iteration, it generates random coordinates and dimensions for either a rectangle or an ellipse, then fills that shape with a color. 

This loop essentially:

Chooses between drawing a rectangle or an ellipse (shape_type).

Generates a random color based on the transaction hash (shape_color).

Defines random coordinates and dimensions for the shape (x1, y1, x2, y2).

Draws the chosen shape with the specified color.

The result is an image with 77 randomly positioned and sized shapes, either rectangles or ellipses, each filled with a unique color based on the transaction hash. The specific appearance of the image will vary each time you run the script due to the random nature of the shape positions, sizes, and colors.

### Colors:

The color is generated using the first 6 characters of the hexadecimal representation of the SHA-256 hash of the transaction hash. The SHA-256 hash produces a hexadecimal string of 64 characters. Each character in a hexadecimal representation can take 16 different values (0-9 and A-F).

Therefore, the number of possible color combinations  equals 16,777,216² 69

### Shapes:

The script randomly selects between a "rectangle" and an "ellipse" for each iteration.
For 69 iterations, you have 2 choices each time, resulting in,

2
69
2 
69

combinations of shapes.


### Patterns (Combination of Colors and Shapes):

Combining colors and shapes, the total number of possible patterns is the product of the possibilities for colors and shapes.
Therefore, the total number of possible patterns is 

((16,777,216² 69))

In practical terms, this results in an extremely large number of possible combinations, providing a wide variety of colors and patterns for your generated images. The specific image generated for a given transaction hash is determined by the random choices made during execution.

### Notes:

Commands:

-  `cd C:\DoginalsHashCanvasCreator`

-  `python auto_doginals_hash_canvas_creator_unique-shapes.py`


-Run this scipt `Hidden_Extractor.py` , and it will reveal and print the hidden transaction ID and Hidden Message:


`cd C:\DoginalsHashCanvasCreator
python Hidden_Extractor.py`


-when asked for file path provide YOUR filepath you saved your inscribed image at:

Example:

C:\DoginalsHashCanvasCreator\hash-map_generated_images\hashmap00006.png

## License
This script is licensed under the MIT License.

Feel free to modify and adapt the script to suit your needs.