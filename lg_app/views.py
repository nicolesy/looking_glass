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
import datetime


def index(request):
    preset_packs = PresetPack.objects.all().order_by("pack_name")
    images = UploadedImage.objects.all()
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login_register'))

    latest_image = request.user.uploaded_images.order_by('timestamp').last()
    
    if latest_image == None:
        return render(request, "lg_app/index.html", {})
    
    processed_images = [] 
        
    if request.method == "POST":
        get_pack_id = request.POST.get("preset_pack_id")
        
        if get_pack_id == None:
            get_pack_id = 7 # this defaults the preset pack to prevent an error if the button is pressed without selecting a preset pack
        
        uploaded_image = request.user.uploaded_images.order_by('timestamp').last()
        code = ''.join([choice(ascii_letters + digits) for i in range(50)])
        user = request.user
        
        pack = PresetPack.objects.get(id=get_pack_id)
        presets = pack.presets.all()
        
        for preset in presets:
            # check if a processed image already exists for this uploaded image and preset
            existing_image = ProcessedImage.objects.filter(user_upload=uploaded_image, preset=preset).first()
            
            if existing_image is not None:
                processed_images.append(existing_image) # appends the list with existing processed images (prevents re-processing)
            
            else:
                lut = pillow_lut.load_cube_file(preset.preset_file.path)
                image = Image.open(uploaded_image.user_img.path)
                image = image.filter(lut)
                watermark(image, text=(preset.preset_name + " (" + pack.pack_name + ") "+ " | nicolesy.com"), pos=(30, 30))
                
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
                    user_upload = uploaded_image,
                    code = code,                    
                )
                preset_applied_image.save()
                processed_images.append(preset_applied_image)
    
    else:
        pack = None # this needs to be here or 'pack' shows up as not defined
        
    
    context = {
        "preset_packs": preset_packs,
        "images": images,
        "latest_image": latest_image,
        "processed_images": processed_images,
        "pack": pack,
    }
    
    if request.user.is_authenticated:
        return render(request, "lg_app/index.html", context)
    else:
        return HttpResponseRedirect(reverse('users:login_register')) #redirects to login page if not registered


def profile_page(request):
    preset_packs = request.user.favorite_packs.all()
    
    context2 = {
        "preset_packs": preset_packs,
    }
    
    if request.user.is_authenticated:
        return render(request, "lg_app/profile.html", context2)
    else:
        return HttpResponseRedirect(reverse('users:login_register')) # redirects to login page if not registered


def about_page(request):
    return render(request, "lg_app/about.html", {})


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
    
    ####### got this code online somewhere :)
    basewidth = 800 #determines the image width ###
    image = Image.open(new_photo.user_img.path)
    wpercent = (basewidth/float(image.size[0])) #resizes
    hsize = int((float(image.size[1])*float(wpercent))) #resizes
    image = image.resize((basewidth,hsize), Image.ANTIALIAS) #resizes
    image.save(new_photo.user_img.path, format='JPEG', quality=80) #sets photo quality and format
    
    
    return HttpResponseRedirect(reverse('lg_app:index'))

# function to add a watermark to the photo (used in the "index" view)
def watermark(photo, text, pos):
    drawing = ImageDraw.Draw(photo)
    white = (255, 255, 255)
    font_path = '~/.fonts/HelveticaNeue.ttc'
    font = ImageFont.truetype(font_path, 18)
    drawing.text(pos, text, fill=white, font=font)
    return photo


# def select_presets(request):
#     presets_get = request.POST.get("preset_dropdown") #this gets the name from the select list
#     preset_packs = PresetPack.objects.all().filter(presets_get)
#     presets = Preset.objects.all().order_by("preset_name")
#     processed_images = latest_image.processed_images.all()
# 
#     context = {}
# 
#     return render(request, "lg_app/index.html", context)
    

# adds a preset pack to the user's wishlist
def add_fave(request, pack_id):
    faves = request.POST['add_pack_fave']
    pack = PresetPack.objects.get(id=pack_id)
    pack.pack_fave.add(request.user)
    
    return HttpResponseRedirect(reverse('lg_app:profile_page'))


# removes a preset pack from the user's wishlist
def delete_fave(request, pack_id):
    delete_fave_id = request.POST['delete_pack_fave']
    delete_fave = PresetPack.objects.get(id=delete_fave_id)
    delete_fave.pack_fave.remove(request.user)
    
    return HttpResponseRedirect(reverse('lg_app:profile_page'))