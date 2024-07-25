from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('board_name', 'order', 'created_time', 'updated_time', 'created_by', 'updated_by')
    list_editable = ('order',)  # ทำให้ฟิลด์ order แก้ไขได้ในหน้ารายการ
    ordering = ('order',)  # เรียงตามฟิลด์ order
    readonly_fields = ('created_time', 'updated_time', 'created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not change:  # ถ้าเป็นการสร้างโมเดลใหม่
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Board, BoardAdmin)
