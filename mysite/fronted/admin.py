from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
  

    list_display = ('board_name','created_time', 'updated_time' ,'created_by', 'updated_by')
    fields = ('board_name', 'user', 'created_time', 'updated_time' ,'created_by', 'updated_by')
    readonly_fields = ('created_time', 'updated_time', 'created_by', 'updated_by')
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Board, BoardAdmin)
