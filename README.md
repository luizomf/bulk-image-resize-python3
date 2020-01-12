# Simple bulk image resize in Python 3

This script will read and resize all images (JPG and PNG) inside a folder and 
sub-folders.
It's going to create new images, not overwrite the old ones. New images will 
have the "_CONVERTED" flag in its name.

## Usage

Create your virtual environment and activate it.

Install requirements.txt

```
pip install -r requirements.txt --user
```

Change the constants.

```
NEW_WIDTH = 640
ROOT_PATH = '/PATH/TO/IMAGES'
```

NEW_WIDTH is the new width you want for your new images. The new height is
going to be calculated automatically to keep the same aspect ratio of the
original image. 
ROOT_PATH is the path to the folder Python will itarate over to find all
images.

