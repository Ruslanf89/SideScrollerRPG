from PIL import Image


def resize_png(input_path, output_path, new_size):
    try:
        # Open the PNG image with transparency
        original_image = Image.open(input_path)

        # Resize the image while preserving transparency
        resized_image = original_image.resize(new_size, Image.ANTIALIAS)

        # Save the resized image as PNG to preserve transparency
        resized_image.save(output_path, format="PNG")

        print(f"Image resized and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Provide the input PNG file path, output path, and new size
    input_file_path = "C:/Users/Dypko/SideScrollerRPG/Sprites/character/Idle/0_Dark_Elves_Idle_000.png"
    output_file_path = "C:/Users/Dypko/SideScrollerRPG/Sprites/character/Idle/1.png"
    new_size = (74, 74)  # Set your desired width and height

    resize_png(input_file_path, output_file_path, new_size)