from PIL import Image
import time

# Generate the number based on the algorithm
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated number: {generated_number}")


def modify_image(input_image_path, output_image_path, n):
    # Open the image
    img = Image.open(input_image_path)
    pixels = img.load()  # Load pixel data

    # Get image dimensions
    width, height = img.size

    # Initialize a variable to store the sum of red pixel values
    red_sum = 0

    # Loop through each pixel in the image
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]  # Get current pixel's RGB values

            # Modify the pixel values by adding n
            new_r = min(r + n, 255)  # Ensure pixel values don't exceed 255
            new_g = min(g + n, 255)
            new_b = min(b + n, 255)

            # Update the pixel in the image with the new RGB values
            pixels[x, y] = (new_r, new_g, new_b)

            # Add the red (r) component to the red sum
            red_sum += new_r

    # Save the modified image
    img.save(output_image_path)

    # Return the sum of all red pixel values
    return red_sum


# Example usage with the generated number
input_image_path = 'images/chapter1.jpg'  # Path to your input image
output_image_path = 'output/chapter1out.png'  # Path to save the modified image

# Modify the image and calculate the sum of red pixel values
red_pixel_sum = modify_image(input_image_path, output_image_path, generated_number)
print(f"The sum of all red pixel values is: {red_pixel_sum}")