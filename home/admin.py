from django.contrib import admin
from .models import Experience, Project, Blog, Comment, Message
from django.utils.html import format_html
from django.contrib.admin.sites import AdminSite


admin.site.site_header = "Clintone Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Clintone's Dashboard"


class CustomAdminSite(AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        context['css'] = 'css/admin.css'  # reference to static file
        return context


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'thumbnail')
    search_fields = ('title', 'company')
    list_filter = ('start_date',)

    def thumbnail(self, obj):
        if obj.title_image:
            return format_html('<img src="{}" style="height:50px;object-fit:cover;border-radius:4px;" />', obj.title_image.url)
        return "-"
    thumbnail.short_description = "Image"

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Message)
admin.site.register(Comment)