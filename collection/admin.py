
from django.contrib import admin

# import your model
from collection.models import Chose

# set up automated slug creation
class ChoseAdmin(admin.ModelAdmin):
    model = Chose
    list_display = ('nom', 'description',)
    prepopulated_fields = {'slug': ('nom',)}

# and register it
admin.site.register(Chose, ChoseAdmin)
