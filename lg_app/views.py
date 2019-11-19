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
    
    latest_image = request.user.uploaded_images.order_by('timestamp').last()
    if latest_image == None:
        return render(request, "lg_app/index.html", {})
    else:
        processed_images = latest_image.processed_images.all()
    
    # context = {
    #     "preset_packs": preset_packs,
    #     "presets": presets,
    #     "images": images,
    #     "latest_image": latest_image,
    #     "processed_images": processed_images,
    # }
    
    data_packs = []
    for preset_pack in preset_packs:
        presets = []
        for preset in preset_pack.presets.all():
            presets.append({
                "name": preset.preset_name,
                "processed_image": ProcessedImage.objects.get(preset_id=preset.id, user_upload_id=latest_image.id).image.url
            })
        data_packs.append({
            "name": preset_pack.pack_name,
            "url": preset_pack.pack_url,
            "description": preset_pack.pack_description,
            "cover": preset_pack.pack_cover,
            "fave": preset_pack.pack_fave,
            "presets": presets,
        })
    

    new_context = {
        "preset_packs": preset_packs,
        "images": images,
        "latest_image": latest_image,
        "processed_images": processed_images,
        "data_packs": data_packs,
    }

    
    if request.user.is_authenticated:
        return render(request, "lg_app/index.html", new_context)
    else:
        return HttpResponseRedirect(reverse('users:login_register'))


def profile_page(request):
    preset_packs = PresetPack.objects.all().order_by("pack_name")
    
    context2 = {
        "preset_packs": preset_packs,
    }
    
    if request.user.is_authenticated:
        return render(request, "lg_app/profile.html", context2)
    else:
        return HttpResponseRedirect(reverse('users:login_register'))


def about_page(request):
    return render(request, "lg_app/about.html", {})


    
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
    request.user.uploaded_images.all().delete() # UploadedImages for the users
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
        basewidth = 800 #determines the image width ###
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


def select_presets(request):
    presets_get = request.POST.get("preset_dropdown") #this gets the name from the select list
    print("=" *100)
    print(presets_get)
    print("=" *100)
    preset_packs = PresetPack.objects.all().filter(presets_get)
    presets = Preset.objects.all().order_by("preset_name")
    processed_images = latest_image.processed_images.all()
    
    context = {}
    
    
    return render(request, "lg_app/index.html", context)