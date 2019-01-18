# Image Recognition Model for Finery

### Packages

- **requests** - used in image download
- **pillow** - image preprocessing, conversion
- **libwebp** - library for reading .webp
- **numpy** 
- **tensorflow (tensorflow-gpu)** - backend for keras
- **keras** - API that is used to construct model

### Files

The `downloadImg.py` will automatically download, categorize and convert images using given link in `dfClean.csv`. These images will be put into their corresponding categories automatically. Note that `dfClean.csv` includes images from sources that are protected by NDA, thus is not shared on the repo.

`modelTraining.ipynb` includes the training code for image recognition models. It demonstrates the process of training ResNet50 and VGG16 models on both binary and multi-class classification. 

`presentationDemo.ipynb` includes the demo code for testing the trained model on given images. It loads models previously trained in `modelTraining.ipynb` and test them on chosen image. Here we include a sample VGG16 model (`best_vgg.hdf5`) that is trained on a similar dataset.
