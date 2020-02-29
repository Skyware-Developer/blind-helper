import os

from imageai.Detection import ObjectDetection
from PIL import Image

image_name = "test4"
image_format = ".jpg"

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image_name + image_format), output_image_path=os.path.join(execution_path , image_name + "new" + image_format))

print("object type - probability")
for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

img = Image.open(image_name + "new" + image_format)
img.show()