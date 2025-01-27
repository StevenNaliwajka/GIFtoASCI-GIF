import time
from PIL import Image, ImageSequence, ImageDraw, ImageFont

# ASCII characters for density levels
ASCII_CHARS = "@%#*+=-:. "

def resize_frame(frame, new_width=100):
    width, height = frame.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # Adjust height for ASCII aspect ratio
    resized_frame = frame.resize((new_width, new_height))
    return resized_frame

def frame_to_grayscale(frame):
    return frame.convert("L")

def map_pixels_to_ascii(gray_frame):
    pixels = gray_frame.getdata()  # Pixel values (0–255)
    ascii_frame = [ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in pixels]
    return "".join(ascii_frame)

def convert_frame_to_ascii(frame, width=100):
    resized_frame = resize_frame(frame, new_width=width)
    gray_frame = frame_to_grayscale(resized_frame)
    ascii_frame = map_pixels_to_ascii(gray_frame)
    ascii_image = "\n".join(
        ascii_frame[i : i + width] for i in range(0, len(ascii_frame), width)
    )
    return ascii_image

def gif_to_ascii(gif_path, width=100, save_path=None):
    try:
        gif = Image.open(gif_path)
        ascii_frames = []  # Store ASCII art frames for the new GIF

        for frame in ImageSequence.Iterator(gif):
            ascii_image = convert_frame_to_ascii(frame, width=width)
            print("\033[H\033[J", end="")  # Clear terminal
            print(ascii_image)

            # Control playback speed
            gif.info["duration"] = gif.info.get("duration", 100)  # Default 100ms
            frame_duration = gif.info["duration"] / 1000  # Convert to seconds
            time.sleep(frame_duration)

            # Save the ASCII frame as an image for the output GIF
            if save_path:
                ascii_frame_image = ascii_to_image(ascii_image, width=width)
                ascii_frames.append(ascii_frame_image)

        # Save the new GIF if requested
        if save_path and ascii_frames:
            ascii_frames[0].save(
                save_path,
                save_all=True,
                append_images=ascii_frames[1:],
                duration=gif.info["duration"],
                loop=0,
            )
            print(f"ASCII GIF saved to {save_path}")

    except FileNotFoundError:
        print(f"Error: File not found at {gif_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def ascii_to_image(ascii_art, width):
    # Load a monospaced font
    try:
        font = ImageFont.truetype("cour.ttf", 12)  # Use Courier font
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font if not available

    # Calculate character dimensions
    char_width, char_height = font.getbbox("A")[2:]  # Character dimensions

    # Calculate the exact image width based on the longest line's pixel width
    draw_test = ImageDraw.Draw(Image.new("RGB", (1, 1)))  # Dummy image to measure text
    max_line_pixel_width = max(
        draw_test.textlength(line, font=font) for line in ascii_art.splitlines()
    )

    img_width = int(max_line_pixel_width)  # Exact width in pixels
    img_height = len(ascii_art.splitlines()) * char_height

    # Create a blank white image
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    # Draw the ASCII art onto the image
    for y, line in enumerate(ascii_art.splitlines()):
        draw.text((0, y * char_height), line, fill="black", font=font)

    return img

