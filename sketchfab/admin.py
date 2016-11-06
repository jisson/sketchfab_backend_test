from django.contrib import admin
from sketchfab.models import Model3d


class Model3dAdmin(admin.ModelAdmin):
    """
    Admin extension for Model3d.
    """
    list_display = ('id', 'name', 'user_username')
    prepopulated_fields = {'slug': ('name',)}

    def user_username(self, obj):
        return obj.user.username


admin.site.register(Model3d, Model3dAdmin)
