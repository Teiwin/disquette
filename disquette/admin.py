from django.contrib import admin

from .models import Disquette, Langue

# admin.site.unregister()
admin.site.register(Disquette)
admin.site.register(Langue)
