from django.contrib import admin

# Register your models here.
# username: samundra
# password: aaerik@#123

from .models import *

admin.site.site_header = "Samundra's Portfolio Admin"

admin.site.register(Contact)
admin.site.register(Blogs)
admin.site.register(Details)
admin.site.register(Skills)