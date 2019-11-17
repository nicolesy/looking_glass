import os 
from looking_glass.settings import BASE_DIR
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Preset, PresetPack, UploadedImage, ProcessedImage
from PIL import Image, ImageDraw, ImageFont
import pillow_lut
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.contrib.auth.decorators import login_required
from string import ascii_letters, digits
from random import choice


def index(request):
    presets = Preset.objects.all().order_by("preset_name")
    preset_packs = PresetPack.objects.all().order_by("pack_name")
    images = UploadedImage.objects.all()
    latest_image = UploadedImage.objects.order_by('timestamp').last()
    processed_images = latest_image.processed_images.all()
    
    data_packs = []
    for preset_pack in preset_packs:
        data_packs.append(preset_pack)
    
    data_processed_images = []
    for image in processed_images:
        data_processed_images.append(image)
    
    print('='*100)
    print(data_processed_images)
    print('='*100)
    
    context = {
        "preset_packs": preset_packs,
        "presets": presets,
        "images": images,
        "latest_image": latest_image,
        "processed_images": processed_images,
        "mydata": {
            "pack_name": data_packs,
            "image_name": data_processed_images,
            }
    }
    
    if request.user.is_authenticated:
        return render(request, "lg_app/index.html", context)
    else:
        return HttpResponseRedirect(reverse('users:login_register'))
    
    
# this is not finished and NEEDS WORK
def get_presets(request):
    db_presets = request.Preset.preset_pack.order_by("preset_name")
    presets = []
    for db_preset in db_presets:
        preset = db_presets.preset_name
        thumbnail = db_presets.preset_thumbnail
        presets.append ({
            "preset": preset,
            "thumbnail": thumbnail,
        })
    
    return JsonResponse({"presets": presets})


# upload a photo and the processed photos are added to the database
@login_required
def upload_photo(request):
    
    request.user.user_img.all().delete() # UploadedImages for the users

    
    upload_photo = request.FILES["upload_photo"]
    user = request.user
    code = ''.join([choice(ascii_letters + digits) for i in range(50)])
    new_photo = UploadedImage(
        user_img = upload_photo,
        user = user,
        code = code,
    )
    new_photo.save()
    
    presets = Preset.objects.all()
    
    
    for preset in presets:
        basewidth = 800 #determines the image width
        lut = pillow_lut.load_cube_file(preset.preset_file.path)
        image = Image.open(new_photo.user_img.path)
        image = image.filter(lut)
        wpercent = (basewidth/float(image.size[0])) #resizes
        hsize = int((float(image.size[1])*float(wpercent))) #resizes
        image = image.resize((basewidth,hsize), Image.ANTIALIAS) #resizes
        
        watermark(image, text=(preset.preset_name + " | nicolesy.com"), pos=(30, 30))
        print("=" *100)
        print(preset.preset_name)
        print("=" *100)
        
        
        image = image.convert('RGB')
        output = BytesIO()
        image.save(output, format='JPEG', quality=100)
        output.seek(0)
        image = InMemoryUploadedFile(output, 'ImageField',
                                    'image.jpg',
                                    'image/jpeg',
                                    sys.getsizeof(output), None)
        
        preset_applied_image = ProcessedImage(
            image = image,
            preset = preset,
            user_upload = new_photo,
            code = code,
            
        )
        preset_applied_image.save()
    
    return HttpResponseRedirect(reverse('lg_app:index'))


def watermark(photo, text, pos):
    drawing = ImageDraw.Draw(photo)
    white = (255, 255, 255)
    font = ImageFont.truetype("HelveticaNeue.ttc", 24)
    drawing.text(pos, text, fill=white, font=font)
    return photo