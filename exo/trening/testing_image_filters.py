from PIL import Image, ImageFilter, ImageEnhance

images = ["1.png", "2.jpg", "3.jpg", "4.jpg"]

image_object = Image.open("images/2.jpg")
# image_object.show()

image_rodents = image_object.convert("L")
# image_rodents.show()

image_filter = image_object.filter(ImageFilter.FIND_EDGES)
# image_filter.show()

image_enhance_contract = ImageEnhance.Contrast(image_object).enhance(5)
# good totayito nice baby
image_enhance_contract.show()
image_enhance_contract.save("images/enhanced_2.jpg")

image_enhance_brightens = ImageEnhance.Brightness(image_object).enhance(2.5)
image_enhance_brightens.show()



