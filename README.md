# Project Looking Glass

*PDX Code Guild Capstone project by Nicole S. Young*

## Project Overview

Part of my business is to create and sell preset packs through my [online store] (https://store.nicolesy.com) in the form of LUT, or .cube, files. Currently on a preset pack product page I show some before/after images of the presets using my images. My goal in this capstope project is to create a website where potential customers can preview their own photos with the presets in my online store.

<img src="https://cdn.shopify.com/s/files/1/0232/9213/products/cheese_2000x.jpg?v=1556058438" title="Teal Orange 04 - Classic" width="200px"> <img src="https://cdn.shopify.com/s/files/1/0232/9213/products/ashlyn_7f676094-755c-4a89-ba68-d16a261ed26b_2000x.jpg?v=1556058434" title="Teal Orange 04 - Contrast" width="200px"> <img src="https://cdn.shopify.com/s/files/1/0232/9213/products/mushrooms_2000x.jpg?v=1556058445" title="Teal Orange 05 - Soft" width="200px">

## Functionality

### Basic features:
- Ability to upload a photo and preview it on the page
- Drop-down with all preset packs, which will show a list of all LUT presets with that pack
- The user can then click on a LUT preset and the preset will apply to their uploaded photo
- Uploaded photo (with preset) will have a simple watermark over the image and right-click disabled
- Users will have the ability to create an account and "favorite" presets they are interested in purchasing
- Main page (without login) will show sample photos to choose from
- If logged-in, the user can upload their own images

### Visuals:
- Nav bar at top with logo, log-in, and links to blog and store
- Image on top (split view or before/after view)
- Watermark over the preset preview image
- Preset packs listed below or in side-nav

### Code:
I'm using the [Pillow LUT] (https://github.com/homm/pillow-lut-tools) Python module to apply the LUT files. The code to apply the LUT file is very simple and is only a few lines of code. One challenge will be to only create temporary jpeg files so that I don't bog down the database with processed files.

```python
from PIL import Image
import pillow_lut

img = Image.open("image.jpg")
lut = pillow_lut.load_cube_file("lut_file.cube")
img.filter(lut).save("temp.jpg")
```

## Data Model

### class = Preset
- **LUT pack title:** Name of the preset pack (ForeignKey)
- **LUT pack URL:** This will link to the preset pack in my online store (CharField)
- **LUT preset name:** Name of the individual preset (CharField)
- **LUT thumbnail:** Image file that represents the preset (ImageField)

### class = PresetPack
- **LUT pack name:** Name of the preset pack
- **LUT pack thumbnail:** Image file that represents the preset pack (ImageField)

### class = UserUpload
- **User Image:** Uploaded file (ImageField)
- **Upload date:** (DateTimeField)

## Schedule

1. Create basic functionality with simple upload and choosing presets from a list
2. Add user login feature to allow for accessing photos and favoriting preset packs
3. Create a split-view of the before/after images (instead of two side-by-side)
4. Create slider for the before/after photo to preview the image
