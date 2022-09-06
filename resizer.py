import os
from PIL import Image

inputDir = 'input'
outputDir = 'output'
original = Image.open('original.png')

print("starting resizer!")

for imageName in os.listdir(inputDir):
    f = os.path.join(inputDir, imageName)
    image = Image.open(f)
    size = image.size

    new_image = original.resize(size)
    new_image.save(os.path.join(outputDir, imageName))
    print(f'{os.path.join(outputDir, imageName)}')

print("Done!")
