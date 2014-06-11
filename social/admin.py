# coding: utf-8

from django.contrib import admin

from models import Person, Org

class PersonAdmin(admin.ModelAdmin):
    list_display = ('f', 'i', 'o', 'tel1', 'prim')
    search_fields = ('f','i','o','tel1','tel2','tel3','addr1','addr2','prim')

    fieldsets = (
        (None, {
            'fields': (('f','i','o'), ('pas','sex')),
        }),
        (u'Телефоны', {
            'fields': (('tel1', 'tel2', 'tel3'))
        }),
        (u'Адреса', {
            'fields': (('addr1', 'addr2'))
        }),
        (None, {
            'fields': (('prim',))
        }),
    )

class PersonInline(admin.TabularInline):
    model = Org.members.through
    verbose_name = "Сотрудник"
    verbose_name_plural = "Сотрудники"
    fields = ('person', 'role')
    extra = 0

class OrgAdmin(admin.ModelAdmin):
    list_display = ('nam', 'addr1', 'prim')
    search_fields = ('nam','addr1','prim')

    inlines = [
        PersonInline,
    ]

admin.site.register(Person, PersonAdmin)
admin.site.register(Org, OrgAdmin)
