from django.contrib import admin

from .models import Owner, Pet


class PetInline(admin.TabularInline):
    model = Pet


class OwnerAdmin(admin.ModelAdmin):
    inlines = [
        PetInline,
    ]


admin.site.register(Pet)
admin.site.register(Owner, OwnerAdmin)
