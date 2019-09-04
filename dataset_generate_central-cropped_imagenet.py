import os
import torch
import torchvision.transforms as transforms
import numbers
from PIL import Image

# configurations
imagenet_path = '/export/scratch/b/libigpu2/datasets/ImageNet2012/'
output_path = '/export/scratch/a/han424/imagenet_central_cropped/'
compressed_path = '/export/scratch/a/han424/imagenet_central_cropped.tar.gz'

# define the train_path and the val_path
input_train_path = imagenet_path + 'train/'
input_val_path = imagenet_path + 'val/'

output_train_path = output_path + 'train/'
output_val_path = output_path + 'val/'

# define the utilities
try:
    import accimage
except ImportError:
    accimage = None

def _is_pil_image(img):
    if accimage is not None:
        return isinstance(img, (Image.Image, accimage.Image))
    else:
        return isinstance(img, Image.Image)

def crop(img, i, j, h, w):
    """Crop the given PIL Image.
    Args:
        img (PIL Image): Image to be cropped.
        i (int): i in (i,j) i.e coordinates of the upper left corner.
        j (int): j in (i,j) i.e coordinates of the upper left corner.
        h (int): Height of the cropped image.
        w (int): Width of the cropped image.
    Returns:
        PIL Image: Cropped image.
    """
    if not _is_pil_image(img):
        raise TypeError('img should be PIL Image. Got {}'.format(type(img)))

    return img.crop((j, i, j + w, i + h))

def center_crop(img):
    w, h = img.size
    output_size = w if (w < h) else h
    if isinstance(output_size, numbers.Number):
        output_size = (int(output_size), int(output_size))
    th, tw = output_size
    i = int(round((h - th) / 2.))
    j = int(round((w - tw) / 2.))
    return crop(img, i, j, th, tw)

def transform_save_image(image_path, save_path):
    # load the image
    img = Image.open(image_path)
    img_crop = center_crop(img) 
    try:
        img_crop.save(save_path)    
    except:
        print('  ' + image_path + ' needs to be transformed from RGBA to RGB before saving to ' + save_path)
        img = img.convert("RGB")
        img.save(save_path)

    return 0

# processing training data
def transform_data_set(input_set_path, output_set_path):
    os.system('mkdir ' + output_set_path)
    for sub_folder in os.listdir(input_set_path):
        sub_folder_path = input_set_path + sub_folder + '/'
        if os.path.isdir(sub_folder_path) is True:
            print('Transforming images from ' + sub_folder_path)
            output_folder_path = output_set_path + sub_folder + '/'
            os.system('mkdir ' + output_folder_path)
            for image_name in os.listdir(sub_folder_path):
                image_path = sub_folder_path + image_name
                image_save_path = output_folder_path + image_name
                transform_save_image(image_path, image_save_path)

# run the transform_data_set function
os.system('mkdir ' + output_path)
transform_data_set(input_train_path, output_train_path)
transform_data_set(input_val_path, output_val_path)

# compress the files
os.system('tar -czvf ' + compressed_path + ' ' + output_path)

        
    
    
