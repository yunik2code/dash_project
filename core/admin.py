from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.History)
admin.site.register(models.Views)
admin.site.register(models.Like)
admin.site.register(models.DisLike)