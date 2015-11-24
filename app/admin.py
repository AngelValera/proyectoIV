from django.contrib import admin
from app.models import Seccion, Producto


# Add in this class to customized the Admin Interface
class SeccionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

class ProductoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Producto, ProductoAdmin)
