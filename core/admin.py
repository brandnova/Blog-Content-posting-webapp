from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Todo)
admin.site.register(Review)
admin.site.register(Team)
admin.site.register(Messages)
admin.site.register(ContactInfo)
admin.site.register(AboutInfo)
admin.site.register(ServiceInfo)
admin.site.register(ServiceList)
admin.site.register(Terms)
admin.site.register(Privacy)

class UserVisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'display_total_visits')
    search_fields = ('user',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['total_visits'] = UserVisit.objects.count()
        return super().changelist_view(request, extra_context=extra_context)

    def display_total_visits(self, obj):
        return obj.user_count()

    display_total_visits.short_description = 'Total Visits'

admin.site.register(UserVisit, UserVisitAdmin)