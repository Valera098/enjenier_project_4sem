from django.contrib import admin
from service.models import Order, User
from import_export import resources
from import_export.admin import ExportMixin, ImportExportModelAdmin
from django.template.defaultfilters import escape
from django.urls import reverse
from django.utils.safestring import mark_safe

@admin.action(description="Change status to verified")
def change_status_true(selfmodeladmin, request, queryset):
    queryset.update(status=True)

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource
    actions = [change_status_true]
    list_filter = ['status']
    list_display = ['id', 'get_tour_id', 'buy_time', 'status']
    search_fields = ['user__username']
    def get_tour_id(self, obj):
        return mark_safe('<a href="{0}?id={1}">{1}</a>'
                .format(reverse("admin:api_tour_changelist"),
                        escape(obj.tour.id)))
    get_tour_id.short_description = 'Tour'