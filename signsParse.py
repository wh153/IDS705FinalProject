import pandas as pd
import os
import numpy as np
import xml.etree.ElementTree as ET
from matplotlib import image
from matplotlib import pyplot
directory = 'annotations'
fileNames = []
fileClassifications = []

for filename in os.scandir(directory):
    xmlParsed = ET.parse(filename.path)
    fileNames.append(xmlParsed.find('filename').text)
    fileClassifications.append(xmlParsed.find('object').find('name').text)

allImages = []

imgDirectory = 'images'
for name in fileNames:
    allImages.append(image.imread('{}/{}'.format(imgDirectory,name)))

