# Doginals TX Hash Super Canvas Creator

## Overview

The Doginals Hash Canvas Creator is a Python script that generates unique and visually appealing images images based on transaction hashes and saves them in the 'generated_images' directory. It pulls ids from the input you provide in (transaction_ids.json). Each image is created dynamically, with cPython Imaging Library (PIL) to create a canvas filled with a variety of random shapes, colors, and patterns. The colors of these shapes, size, and positions are determined by the SHA-256 hash of the transaction, derived from a cryptographic hash function (e.g., SHA-256) to generate a unique hash or binary representation of specific hash transaction id's. The generated images are saved in the PNG format, with the encoded additional information added through steganography.

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

`python auto_doginals_hash_super_canvas_creator.py`

Check Output:
The generated image will be saved in the generated_images directory with the filename based on the provided transaction hash.

## Implementation

The script creates a canvas with a predefined size and fills it with a large number of random shapes, including rectangles, ellipses, triangles, circles, pentagons, hexagons, and stars. The colors of the shapes are determined by hashing random values, providing a unique and vibrant appearance to each image.


## Variants Breakdown
The number of possible variants in each generated image is influenced by several factors:

Number of Shapes: The script draws 300 random shapes, including rectangles, ellipses, triangles, circles, pentagons, hexagons, and stars.

Color Variations: Colors are generated based on the SHA-256 hash of random values, resulting in a vast color palette.

Shape Sizes and Positions: Random coordinates and dimensions are used for each shape, providing a wide range of sizes and positions.

Considering these factors, the DoginalsTX Hash Canvas Creator can generate an enormous number of unique images, each with its own combination of shapes, colors, and patterns. The specific count of possibilities is challenging to calculate precisely but is practically infinite, providing a diverse and visually engaging output.

### Notes:

Commands:

-  `cd C:\DoginalsHashCanvasCreator`


-  `python doginals_hash_super_canvas_creator.py`


-Run this scipt `Hidden_Extractor.py` , and it will reveal and print the hidden transaction ID and Hidden Message:


-  `cd C:\DoginalsHashCanvasCreator
python Hidden_Extractor.py`


-when asked for file path provide YOUR filepath you saved your inscribed image at:

Example:

C:\DoginalsHashCanvasCreator\super-canvas_generated_images\super_canvas00006.png

## License

This script is licensed under the MIT License.

# Happy hashing with The Node Runners Hash Canvas Creator!