from django.contrib import admin
from .models import Preset, PresetPack, UserUpload

admin.site.register(Preset)
admin.site.register(PresetPack)
admin.site.register(UserUpload)


