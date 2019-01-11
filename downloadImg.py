# import dependencies
import requests, sys, os
import random, math
import pandas as pd
from PIL import Image

# import image link file
df = pd.read_csv('dfClean.csv')
x, _ = df.shape

# generate train list of 80% samples, test list of 20% samples
random.seed(0)
trainSplit = random.sample(range(x), math.floor(x*0.8))

# loop through the list and download images
for i in range(x):
    if i in trainSplit:
        group = "train"
    else:
        group = "test"

    imageName = df['imageId'][i]
    imageCategory = df['itemCategory'][i]
    imageLink = df['Links'][i]

    filename = str(group)+"/"+str(imageCategory)+"/"+str(imageName)+".jpg"

    # make folder if folder does not exist
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # escape if mkdir conflict
            if exc.errno != errno.EEXIST:
                raise

    # test connection
    imageConnection = requests.get(imageLink) # get response from link
    if imageConnection.status_code != "404": # continue if image link is valid
        with open(filename,'wb') as f:
            f.write(imageConnection.content) # write image
        try:
            img = Image.open(filename).convert("RGB") # convert image (jpg/webp) to RGB
            img.save(filename, "jpeg") # overwrite saved image
        except IOError:
            os.remove(filename)
            print(str(imageLink)+" failed to convert")
            continue
        print("Downloaded: " + str(filename) + ", " + str(i+1) + "/" + str(x+1))
    else: # skip and log if image link is invalid
        print(str(imageLink)+" is invalid!")
        continue