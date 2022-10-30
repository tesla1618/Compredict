from django.contrib import admin
from .models import Processor, Ram, SSD, HDD, Mobo, GPU

# Register your models here.

admin.site.register(Processor)
admin.site.register(Ram)
admin.site.register(SSD)
admin.site.register(HDD)
admin.site.register(GPU)
admin.site.register(Mobo)