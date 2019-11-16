from django.contrib import admin
from .models import Preset, PresetPack, UploadedImage, ProcessedImage

admin.site.register(Preset)
admin.site.register(PresetPack)
admin.site.register(UploadedImage)
admin.site.register(ProcessedImage)
