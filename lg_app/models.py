from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape


class PresetPack(models.Model):
    pack_name = models.CharField(max_length=100)
    pack_description = models.TextField(max_length=200)
    pack_url = models.CharField(max_length=200)
    pack_thumbnail = models.ImageField(upload_to='images/cover_thumbnails', null=True, blank=True)
    pack_cover = models.ImageField(upload_to='images/cover_images', null=True, blank=True)
    pack_fave = models.BooleanField(default=False)
    
    def __str__(self):
        return self.pack_name
    
    class Meta:
        ordering = [
            'pack_name'
        ]


class Preset(models.Model):
    preset_pack = models.ForeignKey(PresetPack, on_delete=models.CASCADE, related_name='preset_pack')
    preset_name = models.CharField(max_length=200)
    preset_file = models.FileField(upload_to='luts/', null=True, blank=True)
    preset_thumbnail = models.ImageField(upload_to='images/preset_thumbnails', null=True, blank=True)
    
    def show_preset(self):
        return '<img src="%s"/>' % self.preset_thumbnail
        
        show_preset.short_description = 'Thumb'
        show_preset.allow_tags = True
    
    def __str__(self):
        return self.preset_name + " (" + str(self.preset_pack) + ")"

    class Meta:
        ordering = [
            'preset_pack'
        ]


class UploadedImage(models.Model):
    user_img = models.ImageField(upload_to='images/before/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_img')
    timestamp = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username + ' - ' + self.user_img.name



class ProcessedImage(models.Model):
    user_upload = models.ForeignKey(UploadedImage, on_delete=models.CASCADE, related_name = "processed_images")
    image = models.ImageField(upload_to='images/after/')
    preset = models.ForeignKey(Preset, on_delete=models.CASCADE, related_name = "processed_images")
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.preset)



# uploaded_image = UploadedImage.objects.get(id=1)
# uploaded_image.processed_images.all()
# 
# 
# preset = Preset.objects.get(id=1)
# preset.processed_images.all()
