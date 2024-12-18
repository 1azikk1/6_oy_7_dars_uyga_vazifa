from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Species, Flowers


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')
    actions_on_bottom = True
    actions_on_top = False
    search_fields = ('name',)


admin.site.register(Species, SpeciesAdmin)


class FlowersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'views', 'species', 'get_photo', 'is_available')
    list_display_links = ('name', 'id')
    list_editable = ('species', 'is_available')
    readonly_fields = ('views',)
    list_filter = ('species', 'is_available')
    actions_on_bottom = True
    actions_on_top = False
    search_fields = ('name', 'about')

    def get_photo(self, flower):
        if flower.photo:
            return mark_safe(f'<img src="{flower.photo.url}" width="200px">')
        return 'Rasm topilmadi!'

    get_photo.short_description = 'Rasmi'


admin.site.register(Flowers, FlowersAdmin)
