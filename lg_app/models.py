from django.db import models


class PresetPack(models.Model):
    pack_name = models.CharField(max_length=100)
    pack_url = models.CharField(max_length=200)
    pack_thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.pack_name
    
    class Meta:
        ordering = [
            'pack_name'
        ]


class Preset(models.Model):
    preset_pack = models.ForeignKey(PresetPack, on_delete=models.CASCADE)
    preset_name = models.CharField(max_length=200)
    preset_file = models.FileField(upload_to='luts/', null=True, blank=True)
    preset_thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.preset_name
    
    class Meta:
        ordering = [
            'preset_name'
        ]


class UserUpload(models.Model):
    user_img = models.ImageField(upload_to='images/', null=True, blank=True)
    