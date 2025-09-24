from django.apps import AppConfig
from django.contrib.admin.sites import AdminSite

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'


class MyAdminSite(AdminSite):
    site_header = "Clintone Portfolio Admin"
    site_title = "Portfolio Admin"
    index_title = "Welcome to Clintone's Dashboard"

# Use this in place of the default admin site
admin_site = MyAdminSite(name='myadmin')
