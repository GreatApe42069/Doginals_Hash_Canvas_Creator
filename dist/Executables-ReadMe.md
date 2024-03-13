# Hidden_Encoder.exe
## Usage
***The executables operate independently of Python.***

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