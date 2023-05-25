from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    #propiedades que quiero que se muestren...
    list_display=('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    # quiero que cuando le de click a una columna me linke hacia el detalle del usuario
    list_display_link =('email', 'first_name', 'last_name')
    # los campos de lectura sean solo de last_login y date_joined para que me diga cuando fue la última vez que se logueo y cuando fue
    readonly_fields = ('last_login', 'date_joined')
    # ordenar por fecha ascendente
    ordering = ('-date_joined',)


    # filtro horizontal
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Para registrar el modelo
admin.site.register(Account, AccountAdmin)

