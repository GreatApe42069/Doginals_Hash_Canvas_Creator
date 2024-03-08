from PIL import Image, ImageDraw
import hashlib
import os
import random
import math
import json
from stegano import lsb

def create_super_canvas_generated_images_directory():
    directory = 'super-canvas_generated_images'
    if not os.path.exists(directory):
        os.makedirs(directory)

def render_image(transaction_hash):
    create_super_canvas_generated_images_directory()

    # Create a unique image based on the transaction hash
    image_size = (500, 500)
    image = Image.new("RGB", image_size, get_random_background_color())
    draw = ImageDraw.Draw(image)

    # Use the transaction hash to seed the random number generator
    hash_as_int = int.from_bytes(hashlib.sha256(transaction_hash.encode()).digest(), byteorder='big')
    random.seed(hash_as_int)

    # Draw a large number of random shapes
    for _ in range(300):
        shape_type = random.choice(["rectangle", "ellipse", "triangle", "circle", "pentagon", "hexagon", "star"])
        shape_color = get_random_shape_color()

        x1, y1, x2, y2 = get_random_shape_coordinates(image_size)

        if shape_type == "rectangle":
            draw.rectangle([x1, y1, x2, y2], fill=shape_color)
        elif shape_type == "ellipse":
            draw.ellipse([x1, y1, x2, y2], fill=shape_color)
        elif shape_type == "triangle":
            draw.polygon([(x1, y1), (x2, y2), ((x1 + x2) // 2, y1)], fill=shape_color)
        elif shape_type == "circle":
            draw.ellipse([x1, y1, x2, y2], fill=shape_color)
        elif shape_type == "pentagon":
            draw.polygon(get_polygon_vertices(x1, y1, x2, y2, 5), fill=shape_color)
        elif shape_type == "hexagon":
            draw.polygon(get_polygon_vertices(x1, y1, x2, y2, 6), fill=shape_color)
        elif shape_type == "star":
            draw.polygon(get_star_vertices(x1, y1, x2, y2), fill=shape_color)

    # Save the image in the 'super-canvas_generated_images' directory
    image_path = f"super-canvas_generated_images/{transaction_hash}_steg.png"

    # Encode both the transaction ID and a message and hide them
    encoded_message = f"{transaction_hash}|||WE ARE THE NODE RUNNERS You Cant Bootleg Our Shit!!!"
    steg_image = lsb.hide(image, encoded_message)

    # Save the final steganographed image
    steg_image.save(image_path)

    # Return the path to the generated image with steganography
    return image_path

def get_random_background_color():
    return "#" + hashlib.sha256(str(random.randint(0, 255)).encode()).hexdigest()[:6]

def get_random_shape_color():
    return "#" + hashlib.sha256(str(random.randint(0, 255)).encode()).hexdigest()[:6]

def get_random_shape_coordinates(image_size):
    x1 = random.randint(0, image_size[0] - 1)
    y1 = random.randint(0, image_size[1] - 1)
    x2 = x1 + random.randint(1, image_size[0] - x1)
    y2 = y1 + random.randint(1, image_size[1] - y1)
    return x1, y1, x2, y2

def get_polygon_vertices(x1, y1, x2, y2, sides):
    angle = 360 / sides
    vertices = []

    for i in range(sides):
        angle_rad = math.radians(i * angle)
        x = x1 + (x2 - x1) / 2 + (x2 - x1) / 2 * math.cos(angle_rad)
        y = y1 + (y2 - y1) / 2 + (y2 - y1) / 2 * math.sin(angle_rad)
        vertices.append((x, y))

    return vertices

def get_star_vertices(x1, y1, x2, y2):
    outer_radius = (x2 - x1) / 2
    inner_radius = outer_radius / 2
    angle = 360 / 5
    vertices = []

    for i in range(5):
        outer_angle_rad = math.radians(i * angle)
        inner_angle_rad = math.radians((i + 0.5) * angle)
        x_outer = x1 + (x2 - x1) / 2 + outer_radius * math.cos(outer_angle_rad)
        y_outer = y1 + (y2 - y1) / 2 + outer_radius * math.sin(outer_angle_rad)
        x_inner = x1 + (x2 - x1) / 2 + inner_radius * math.cos(inner_angle_rad)
        y_inner = y1 + (y2 - y1) / 2 + inner_radius * math.sin(inner_angle_rad)
        vertices.extend([(x_outer, y_outer), (x_inner, y_inner)])

    return vertices

def process_transaction_ids(transaction_ids_json):
    for transaction_id_json in transaction_ids_json:
        # Extract the transaction ID from the dictionary
        transaction_id = transaction_id_json['TransactionID']
        image_path = render_image(transaction_id)
        print(f"Image generated and saved at: {image_path}")

# Example usage with multiple transaction IDs from a JSON file
if __name__ == "__main__":
    # Load transaction IDs from a JSON file
    with open("transaction_ids.json", "r") as json_file:
        transaction_ids_json = json.load(json_file)

    # Process the transaction IDs
    process_transaction_ids(transaction_ids_json)
