
from PIL import Image

image_object = Image.open("images/1.png")
image_object.show()
width, height = image_object.size

for x in range(width):
    for y in range(height):

        pixel_coordination = (x, y)
        r, g, b = image_object.getpixel(pixel_coordination)

        negative_color = (255-r, 255-g, 255-b)
        image_object.putpixel(pixel_coordination, negative_color)

image_object.show()
