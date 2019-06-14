from django.contrib import admin
from cmdb.models import *

class ServersAdmin(admin.ModelAdmin):
    list_display = ('roles','usage','pub_ipaddress','private_ipaddress','customer','password','cpu','mem','bandwidth','port')
    search_fields = ['roles']
    list_filter = ['usage']
admin.site.register(Csp)
admin.site.register(Company)
admin.site.register(Servers,ServersAdmin)
admin.site.register(Group)

