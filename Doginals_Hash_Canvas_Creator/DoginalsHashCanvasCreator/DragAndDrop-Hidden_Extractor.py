from stegano import lsb
from PIL import Image
import sys
import os
import json

def extract_hidden_message(image_path):
    try:
        # Load the steganographed image
        steg_image = lsb.reveal(Image.open(image_path))

        # Check if the hidden message contains '|||'
        if '|||' in steg_image:
            # Split the hidden message (transaction ID and phrase) using '|||'
            hidden_values = steg_image.split('|||')

            # Extract the hidden transaction ID and phrase
            hidden_transaction_id = hidden_values[0]
            hidden_phrase = hidden_values[1]

            # Print the extracted transaction ID and phrase
            print("Extracted Transaction ID:", hidden_transaction_id)
            print("Extracted Hidden Phrase:", hidden_phrase)

            # Create a folder for extracted hidden messages if it doesn't exist
            folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Extracted_Hidden_Messages_Captured")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Create a JSON file with the extracted hidden message
            json_data = {"TransactionID": hidden_transaction_id, "HiddenPhrase": hidden_phrase}
            json_file_path = os.path.join(folder_path, "extracted_hidden_message.json")
            with open(json_file_path, "w") as json_file:
                json.dump(json_data, json_file, indent=4)

            print(f"Extracted hidden message saved to: {json_file_path}")
        else:
            print("No hidden message found in the image.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if an image file was dragged and dropped onto the script
    if len(sys.argv) > 1:
        # The first argument is the script name, so the second argument is the image file path
        image_path = sys.argv[1]
        extract_hidden_message(image_path)
    else:
        print("Please drag and drop an image file onto the script.")
