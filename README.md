# Image Recognition Model for Finery

### Packages

- **requests** - used in image download
- **pillow** - image preprocessing, conversion
- **libwebp** - library for reading .webp
- **numpy** 
- **tensorflow (tensorflow-gpu)** - backend for keras
- **keras** - API that is used to construct model

### Files

The `downloadImg.py`  demonstrates how we automatically download, categorize and convert images using links in `dfClean.csv`, which contains the sources of training images. These images will be put into their corresponding categories automatically. Note that `dfClean.csv` includes images from sources that are protected by NDA, thus is not shared on the repo.

`Training.ipynb` includes the training code for image recognition models. It demonstrates the process of training ResNet50 and VGG16 models on both binary and multi-class classification. 

`Demo.ipynb` includes the demo code for testing the trained model on given images. It loads models previously trained in `Training.ipynb` and test them on chosen image (stored in `\img`). Here we include a VGG16 model (`best_vgg.hdf5`) that is trained on Similar data. Here we also use `labelDecode.py` as helper function to decode the prediction array.

