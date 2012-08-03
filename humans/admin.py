from django.contrib import admin

from humans.models import HumanGroup, Handle, Human, Snippet, HandleType

admin.site.register(HumanGroup)
admin.site.register(Handle)
admin.site.register(Human)
admin.site.register(Snippet)
admin.site.register(HandleType)
