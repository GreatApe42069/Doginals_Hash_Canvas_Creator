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
    # Prompt the user to input the image path
    image_path = input("Enter the image path: ")

    # Prompt the user to input the hidden message
    hidden_message = input("Enter the hidden message: ")

    # Encode the message for the provided image
    encode_message(image_path, hidden_message)
