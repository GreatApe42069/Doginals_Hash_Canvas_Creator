from PIL import Image, ImageDraw
import hashlib
import os
import random
import json
from stegano import lsb  # Import the lsb module

def create_hash_map_generated_images_directory():
    directory = 'hash-map_generated_images'
    if not os.path.exists(directory):
        os.makedirs(directory)

def render_image(transaction_id):  # Change the parameter name to transaction_id
    create_hash_map_generated_images_directory()

    # Create a unique image based on the transaction ID
    image_size = (500, 500)
    image = Image.new("RGB", image_size, "black")
    draw = ImageDraw.Draw(image)

    # Use the transaction ID to seed the random number generator
    random.seed(int(transaction_id, 16))

    # Draw random shapes
    for _ in range(69):
        shape_type = random.choice(["rectangle", "ellipse"])
        shape_color = "#" + hashlib.sha256(str(transaction_id).encode()).hexdigest()[:6]

        x1 = random.randint(0, image_size[0] - 50)
        y1 = random.randint(0, image_size[1] - 50)
        x2 = x1 + random.randint(33, 69)
        y2 = y1 + random.randint(22, 77)

        if shape_type == "rectangle":
            draw.rectangle([x1, y1, x2, y2], fill=shape_color)
        elif shape_type == "ellipse":
            draw.ellipse([x1, y1, x2, y2], fill=shape_color)

    # Encode the transaction ID and a message and hide them
    encoded_message = f"{transaction_id}|||WE ARE THE NODE RUNNERS You Cant Bootleg Our Shit!!!"
    steg_image = lsb.hide(image, encoded_message)

    # Save the final steganographed image
    steg_image_path = f"hash-map_generated_images/{transaction_id}_steg.png"
    steg_image.save(steg_image_path)

    # Return the path to the generated image with steganography
    return steg_image_path

def process_transaction_ids(transaction_ids):
    for transaction_dict in transaction_ids:
        # Extract the transaction ID from the dictionary
        transaction_id = transaction_dict.get('TransactionID', '')
        if transaction_id:
            image_path = render_image(transaction_id)
            print(f"Steganographed Image generated and saved at: {image_path}")

# Example usage with multiple transaction IDs from a JSON file
if __name__ == "__main__":
    # Load transaction IDs from a JSON file
    with open("transaction_ids.json", "r") as json_file:
        transaction_ids = json.load(json_file)

    # Process the transaction IDs
    process_transaction_ids(transaction_ids)
