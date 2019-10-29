# i am using the pip 19.2.3

from PIL import Image


def resize_images(list_of_images, new_size=(200, 200)):
    for index in list_of_images:
        image = Image.open("images/" + index)
        image = image.resize(new_size)
        image.save("images/new_" + index)
        # image.show()


images = ["1.png", "2.jpg", "3.jpg", "4.jpg"]

print("the prosses starting")
resize_images(images)
print("the prosses stoped")
