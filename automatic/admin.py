from django.contrib import admin

from automatic.models import Worker, PointSale, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')
    list_display_links = ('id', 'name', )
    search_fields = ('name',)


@admin.register(PointSale)
class PointSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'worker')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Visit)
class VisitSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'point_sale')
    list_display_links = ('id', 'point_sale')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

