from django.contrib import admin
import main_app.models as _

# Register your models here.
admin.site.register(_.User)
admin.site.register(_.Medicamento)
admin.site.register(_.TipoMedicamento)
admin.site.register(_.Pedido)
admin.site.register(_.Compra)
admin.site.register(_.TarjetaEstiba)
