# Doginals Hash Canvas Creator

-The Doginals Hash Canvas Creator is a set of Python scripts that allow you to create, encode, and decode images with hidden messages using the Least Significant Bit (LSB) method and steganography. These scripts are designed to generate unique and visually appealing hash-based images that are encoded with hidden data, derived from a cryptographic hash function (e.g., SHA-256) to generate a unique hash or binary representation of specific hash transaction id's. The generated images are saved in the PNG format.

## Scripts Overview

### 1. Hidden_Encoder.py

The `Hidden_Encoder.py` script is used to encode hidden messages into images. It takes image paths and corresponding messages from a JSON file and saves the encoded images in the specified directory.

**Usage:**

`python Hidden_Encoder.py`

*Ensure that the 'C:/DoginalsHashCanvasCreator/encoded_images' directory exists before running the script.*

### 2. Hidden_Extractor.py

The `Hidden_Extractor.py` script is designed to reveal hidden messages from steganographed images. This script decodes hidden messages from steganographed images using the Least Significant Bit (LSB) technique Users input the path to the steganographed image, and the script extracts and prints the hidden information.

**Usage:**

`python Hidden_Extractor.py`

### 3. auto_doginals_hash_canvas_creator.py

The `auto_doginals_hash_canvas_creator.py` script generates hash-based images with random shapes. It uses a set of transaction IDs as input and creates visually unique images for each Tx ID. This script generates unique colored block images based on transaction hashes and saves them in the 'generated_images' directory. Each image is created dynamically, with colors derived from a cryptographic hash function (e.g., SHA-256) to generate a unique hash or binary representation of specific hash transaction id's. The generated images are saved in the PNG format, with the encoded additional information added through steganography.

**Usage:**

`python auto_doginals_hash_canvas_creator.py`

### 4. auto_doginals_hash_canvas_creator_unique-shapes.py

Similar to the previous script, `auto_doginals_hash_canvas_creator_unique-shapes.py` generates hash-based images but with a focus on unique shapes for each image. This script creates images based on transaction hashes and saves them in the 'generated_images' directory. Each image is created dynamically, with colors, and containing randomly placed rectangles and ellipses. The colors of these shapes are determined by the SHA-256 hash of the transaction. derived from a cryptographic hash function (e.g., SHA-256) to generate a unique hash or binary representation of specific hash transaction id's. The generated images are saved in the PNG format, with the encoded additional information added through steganography. 


**Usage:**

python auto_doginals_hash_canvas_creator_unique-shapes.py

### 5. doginals_hash_super_canvas_creator.py

The `doginals_hash_super_canvas_creator.py` script creates hash-based images with a combination of unique shapes. It is designed to produce visually appealing and complex compositions.This script generates unique and visually appealing images images based on transaction hashes and saves them in the 'generated_images' directory. Each image is created dynamically, with cPython Imaging Library (PIL) to create a canvas filled with a variety of random shapes, colors, and patterns. The colors of these shapes, size, and positions are determined by the SHA-256 hash of the transaction, derived from a cryptographic hash function (e.g., SHA-256) to generate a unique hash or binary representation of specific hash transaction id's. The generated images are saved in the PNG format, with the encoded additional information added through steganography

**Usage:**

python doginals_hash_super_canvas_creator.py

#### Prerequisites:

**Install dependencies:

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
 

#### Notes:

Follow the specific usage instructions in ReadMe's for each script mentioned above.

**Commands:**

`cd C:\DoginalsHashCanvasCreator`

`python auto_doginals_hash_canvas_creator.py`

`python auto_doginals_hash_canvas_creator_unique-shapes.py`

`python doginals_hash_super_canvas_creator.py`


-Run this scipt `Hidden_Encoder.py` , and it will encode the hidden Hidden Message for new mints and collections:

`cd C:\DoginalsHashCanvasCreator
python Hidden_Encoder.py`

-Run this scipt `Hidden_Extractor.py` , and it will reveal and print the hidden transaction ID and Hidden Message:


`cd C:\DoginalsHashCanvasCreator
python Hidden_Extractor.py`


-when asked for file path provide YOUR filepath you saved your inscribed image at:

**Examples:**

C:\DoginalsHashCanvasCreator\encoded_images\ape-with-sign.png_encoded.png

C:\DoginalsHashCanvasCreator\hash-map_generated_images\hashmap00006.png

C:\DoginalsHashCanvasCreator\super-canvas_generated_images\ape-neon-cutout.png_encoded.png


*For any issues or further assistance, feel free to open an issue on the repository.*

# Happy hashing with The Node Runners Hash Canvas Creator!