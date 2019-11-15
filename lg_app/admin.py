from django.contrib import admin
from .models import Preset, PresetPack, UserUpload, PresetApplied

admin.site.register(Preset)
admin.site.register(PresetPack)
admin.site.register(UserUpload)
admin.site.register(PresetApplied)
