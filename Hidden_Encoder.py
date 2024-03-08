from stegano import lsb
from PIL import Image
import json
import os

def encode_message(image_path, hidden_message):
    try:
        # Load the image
        image = Image.open(image_path)

        # Encode the hidden message in the image using LSB
        steg_image = lsb.hide(image, f'|||{hidden_message}')  # Include '|||' delimiter

        # Ensure the 'encoded_images' directory exists
        os.makedirs("C:/DoginalsHashCanvasCreator/encoded_images", exist_ok=True)

        # Save the steganographed image
        steg_image.save(f"C:/DoginalsHashCanvasCreator/encoded_images/{os.path.basename(image_path)}_encoded.png")

        print(f"Message encoded successfully for {os.path.basename(image_path)}")
    except Exception as e:
        print(f"Error encoding message for {os.path.basename(image_path)}: {e}")

def encode_messages_from_json(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

            for entry in data:
                image_path = entry.get('image_path', '')
                hidden_message = entry.get('hidden_message', '')

                if image_path and hidden_message:
                    encode_message(image_path, hidden_message)
                else:
                    print(f"Invalid entry in JSON file: {entry}")
    except Exception as e:
        print(f"Error loading JSON file: {e}")

if __name__ == "__main__":
    # JSON file containing image paths and corresponding hidden messages
    json_file_path = "C:/DoginalsHashCanvasCreator/encoded_messages.json"

    # Uncomment and use one of the following examples:

    # Example 1: Encode messages for individual images
    # encode_message("path/to/image1.png", "This is a secret message for image 1")
    # encode_message("path/to/image2.png", "Another secret message for image 2")

    # Example 2: Encode messages for multiple images from a JSON file
    encode_messages_from_json(json_file_path)
