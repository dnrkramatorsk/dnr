# coding: utf-8

from django.contrib import admin

from models import Call

class CallAdmin(admin.ModelAdmin):
    list_display = ('date', 'phone', 'author', 'title', 'message', 'closed', 'user')
    search_fields = ('phone','author','title','message')
    exclude = ('user',)
    list_filter = ('date', 'user', 'closed')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Call, CallAdmin)
