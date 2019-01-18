######################################################################
##########   This is helper code for labeling predictions   ##########
######################################################################

import numpy as np

dic = ["Tops",
       "Pants",
       "Skirts & Overalls",
       "Dresses",
       "Jackets",
       "Sportswear",
       "Underwear",
       "Shoes",
       "Bags",
       "Accessories",
       "Miscs & Lingeries",
       "Non-wardrobe"]

def decodeScore(arr):
       for label, score in zip(dic, arr.tolist()[0]):
              print("{} : {:.2%}".format(label, score))