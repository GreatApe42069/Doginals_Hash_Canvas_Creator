# Doginals Hash Canvas Creator

-The Doginals Hash Canvas Creator is a set of Python scripts that allow you to create, encode, and decode images with hidden messages using the Least Significant Bit (LSB) method and steganography. These scripts are designed to generate unique and visually appealing hash-based images that are encoded with hidden data, derived from a cryptographic hash function (e.g., SHA-256) to generate a unique hash or binary representation of specific hash transaction id's which it gets from your provided inputs in (transaction_ids.json). The generated images are saved in the PNG format.

***You can Independently run scripts or run executables, its your preference. The executable operates independently of Python. I did this so users without python can use it too***

# Hidden_Encoder.exe
## Usage

- ***Enter file path and Hidden message inside the ((`encoded_messages.json`)) inside the Main folder not in dist folder , in the Main folder. Make sure to use double    \\  if you use  \  in file path input you will get, Error loading JSON file: Invalid \escape: line 3 column 26 (char 33)***

- Hidden_Encoder.exe should be run from the command line, in command prompt, If you use for Building App its perfect but closes command prompt a little fast when viewing the hidden message, so opening command prompt and manually using this script and exe works best if you want hidden messaed displayed for a prolonged period.

The script will encode the hidden message in the provided image and save the steganographed image in the encoded_images directory. **Note: when using executables files save in dist folders under same folder name e.g. `generated_images`, `hash-map_generated_images`, etc

## Implementation
The Hidden_Encoder.exe executable is created from the Hidden_Encoder.py script. It utilizes the stegano and Pillow libraries to encode hidden messages in images. Ensure that Python is not required, as the executable is standalone.

# Hidden_Decoder.exe
##Usage
Double-click on Hidden_Decoder.exe or run it from the command line.

Enter the steganographed image file path when prompted.

The script will decode the hidden message from the provided steganographed image and display the extracted transaction ID and hidden phrase.

## Implementation
The Hidden_Decoder.exe executable is generated from the Hidden_Decoder.py script. It relies on the stegano and Pillow libraries for decoding hidden messages. This executable is independent and doesn't require a separate Python environment.

# Super_Canvas_Creator.exe
## Usage
Double-click on Super_Canvas_Creator.exe or run it from the command line.

The script will generate a unique and visually appealing image based on the transaction hashes provided in the transaction_ids.json file.

The resulting steganographed images will be saved in the super-canvas_generated_images directory.

## Implementation
The Super_Canvas_Creator.exe executable is derived from the Super_Canvas_Creator.py script. It utilizes the stegano, Pillow, and hashlib libraries to create visually diverse images based on transaction hashes. The executable operates independently of Python.

***Note: Ensure that the necessary JSON files (transaction_ids.json) are present in the same directory as the executables for seamless execution. Modify file paths in the scripts if required.***

## Scripts Overview

### 1. Hidden_Encoder.py

The `Hidden_Encoder.py` script is used to encode hidden messages into images. It takes image paths and corresponding messages from a JSON file and saves the encoded images in the specified directory.

**Usage:**

***Enter file path and Hidden message inside the ((`encoded_messages.json`)) inside the Main folder not in dist folder , in the Main folder. Make sure to use double    \\  if you use  \  in file path input you will get, Error loading JSON file: Invalid \escape: line 3 column 26 (char 33)***

`python Hidden_Encoder.py`

*Ensure that the 'C:/DoginalsHashCanvasCreator/encoded_images' directory exists before running the script.*

### 2. Hidden_Extractor.py

The `Hidden_Extractor.py` script is designed to reveal hidden messages from steganographed images. This script decodes hidden messages from steganographed images using the Least Significant Bit (LSB) technique Users input the path to the steganographed image, and the script extracts and prints the hidden information.

**Usage:**

*** For Using just the .py script, Enter Transaction ID's inside the ((`transaction_ids.json`)) **inside the Main folder if your using the individual python script NOT the one in dist folder, if you use the EXE version, then you DONT use ((`transaction_ids.json`)) in the Main folder, you put your input for ((`transaction_ids.json`)) ONLY inside the "dist" folder this time. Make sure to use double  \\  if you use  \  in the file path input you will get, Error loading JSON file: Invalid \escape: line 3 column 26 (char 33)***

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