from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(StudyGroup)
admin.site.register(Student)

class SettingAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False if self.model.objects.count() > 0 else super().has_delete_permission(request)

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

admin.site.register(Setting, SettingAdmin)
admin.site.register(FAQ)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Action)