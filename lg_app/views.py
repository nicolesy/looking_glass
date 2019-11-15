import os 
from looking_glass.settings import BASE_DIR
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Preset, PresetPack, UserUpload, PresetApplied
from PIL import Image
import pillow_lut
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def index(request):
    presets = Preset.objects.all().order_by("preset_name")
    preset_packs = PresetPack.objects.all().order_by("pack_name")
    images = UserUpload.objects.all()
    latest_image = UserUpload.objects.order_by('timestamp').first()
    
    
    context = {
        "preset_packs": preset_packs,
        "presets": presets,
        "images": images,
        "latest_image": latest_image,
    }
    
    return render(request, "lg_app/index.html", context)
    
    
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
# @login_required
def upload_photo(request):
    upload_photo = request.FILES["upload_photo"]
    user = request.user
    # print(request.FILES["upload_photo"])
    new_photo = UserUpload(
        user_img = upload_photo,
        user = user,
    )
    new_photo.save()
    
    print('='*100)
    print(new_photo.user_img)
    # print('saving file to ' + output_path)
    print('='*100)
    
    presets = Preset.objects.all()
    
    for preset in presets:
        image = apply_lut(new_photo, preset)
        preset_applied_image = PresetApplied(
            image = image,
            preset = preset,
            user_upload = new_photo,
        )
        preset_applied_image.save()
    
    # loop over the presets
    # apply the lut and generate a new image
    # for each preset, create a PresetApplied and save it
    
    return HttpResponseRedirect(reverse('lg_app:index'))


# function to apply the LUT file to an image
def apply_lut(img, cube):
    # lut = pillow_lut.load_cube_file(os.path.join(BASE_DIR, 'uploads', str(cube.preset_file)))
    # output_path = str(cube.id) + '.jpg'
    
    lut = pillow_lut.load_cube_file(cube.preset_file.path)
    
    image = Image.open(img.user_img.path)
    image = image.filter(lut)
    
    f = BytesIO()
    try:
        image.save(f, format='jpeg')
        img.user_img.save(img.user_img.path,
                                       ContentFile(f.getvalue()))
    #model_instance.save()
    finally:
        f.close()
    
    
    final_image.save(output_path)
    return final_image
