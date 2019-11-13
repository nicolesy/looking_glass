from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Preset, PresetPack, UserUpload



def index(request):
    presets = Preset.objects.all().order_by("preset_name")
    preset_packs = PresetPack.objects.all().order_by("pack_name")
    
    context = {
        "preset_packs": preset_packs,
        "presets": presets,
    }
    
    return render(request, "lg_app/index.html", context)
    
