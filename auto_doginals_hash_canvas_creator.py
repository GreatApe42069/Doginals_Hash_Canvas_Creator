from PIL import Image, ImageDraw
import hashlib
import os
import json
from stegano import lsb

def create_generated_images_directory():
    directory = 'generated_images'
    if not os.path.exists(directory):
        os.makedirs(directory)

def render_image(transaction_id_json):
    create_generated_images_directory()

    # Extract the transaction ID from the dictionary
    transaction_id = transaction_id_json['TransactionID']

    # Create a unique image based on the transaction ID
    image_size = (500, 500)
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Use the first 6 characters of the transaction ID to generate a color
    color = "#" + hashlib.sha256(transaction_id.encode()).hexdigest()[:6]

    # Draw a rectangle with the generated color
    draw.rectangle([0, 0, image_size[0], image_size[1]], fill=color)

    # Encode the transaction ID and a message and hide them
    encoded_message = f"{transaction_id}|||WE ARE THE NODE RUNNERS You Cant Bootleg Our Shit!!!"
    steg_image = lsb.hide(image, encoded_message)

    # Save the final steganographed image
    steg_image_path = f"generated_images/{transaction_id}_steg.png"
    steg_image.save(steg_image_path)

    # Return the path to the generated image with steganography
    return steg_image_path

def process_transaction_ids(transaction_ids_json):
    for transaction_id_json in transaction_ids_json:
        steg_image_path = render_image(transaction_id_json)
        print(f"Steganographed Image generated and saved at: {steg_image_path}")

# Example usage with multiple transaction IDs from a JSON file
if __name__ == "__main__":
    # Load transaction IDs from a JSON file
    with open("transaction_ids.json", "r") as json_file:
        transaction_ids_json = json.load(json_file)

    # Process the transaction IDs
    process_transaction_ids(transaction_ids_json)
