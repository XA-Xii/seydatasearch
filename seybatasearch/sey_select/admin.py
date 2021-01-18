from django.contrib import admin

# Register your models here.

from sey_select.models import seyvalue,seymaterial,Seytext

admin.site.register(seyvalue)
admin.site.register(seymaterial)
admin.site.register(Seytext)