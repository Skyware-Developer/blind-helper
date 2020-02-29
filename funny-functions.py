import base64

def image_to_string():
    with open("test1.jpg", "rb") as image_file:
        img_coded = base64.b64encode(image_file.read())
    print("The image was coded.")
    return(img_coded)

def string_to_image(b64_str):
    imgdata = base64.b64decode(b64_str)
    filename = "img_converted.jpg"
    with open(filename, 'wb') as f:
        f.write(imgdata)
    print('Image Created')

# string_to_image(image_to_string())