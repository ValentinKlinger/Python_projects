from PIL import Image
from math import ceil


def img_to_ascii(
    image_path: str,
    width: int = None,
    height: int = None,
    quality: float = 1.0,
    ascii_caracters: tuple[str] = (" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"),
) -> str:
    """
    Return a ascii art of a picture.
    """
    img = Image.open(image_path)
    if width == None:
        width = int(img.size[0] * quality)
    if height == None:
        height = int(img.size[1] * quality)

    img = img.resize((width, height))
    output = ""
    for i in range(height):
        for j in range(width):
            pixel_color = img.getpixel((j, i))
            shade_gray = (pixel_color[0] + pixel_color[1] + pixel_color[2]) // 3
            ascii_caracter = shade_gray // ceil(255 / len(ascii_caracters))
            output += ascii_caracters[ascii_caracter] + " "
        output += "\n"
    return output


if __name__ == '__main__':
    print(img_to_ascii("/image/path", quality=0.1))
