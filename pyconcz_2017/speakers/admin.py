from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from django.contrib import admin
from .models import Speaker, Talk, Slot, Workshop


class SlotAdmin(admin.ModelAdmin):
    list_display = ['date', 'get_description', 'room']
    list_filter = ['room']
    date_hierarchy = 'date'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('content_object')

    def get_description(self, obj):
        return obj.content_object or obj.description


class SpeakerResource(resources.ModelResource):

    class Meta:
        model = Speaker
        fields = export_order = (
            'full_name', 'keynote',
            'email', 'github', 'twitter',
        )


class SpeakerAdmin(ImportExportActionModelAdmin):
    list_display = ['full_name', 'get_talks', 'get_workshops', 'keynote', 'display_position']
    list_filter = ['keynote', ]
    search_fields = ['full_name', 'email', 'github', 'twitter', ]
    resource_class = SpeakerResource

    def get_talks(self, obj):
        return ', '.join([t.title for t in obj.talks.all()])
    get_talks.short_description = 'talks'

    def get_workshops(self, obj):
        return ', '.join([w.title for w in obj.workshops.all()])
    get_workshops.short_description = 'workshops'


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk)
admin.site.register(Workshop)
admin.site.register(Slot, SlotAdmin)
