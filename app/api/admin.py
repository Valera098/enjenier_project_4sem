from django.contrib import admin
from api.models import Resort, Country, Tour
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.template.defaultfilters import escape
from django.urls import reverse
from django.utils.safestring import mark_safe

class ResortResource(resources.ModelResource):
    class Meta:
        model = Resort
@admin.register(Resort)
class ResortAdmin(ImportExportModelAdmin):
    resource_class = ResortResource
    list_display = ['name', 'get_country_name']
    search_fields = ['name', 'country__name']
    def get_country_name(self, obj):
        return mark_safe('<a href="{0}?q={1}">{1}</a>'
                        .format(reverse("admin:api_country_changelist"), escape(obj.country.name)))
    get_country_name.short_description = 'Country'

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource
    list_display = ['id', 'name', 'code', 'iso_code']
    search_fields = ['name', 'iso_code']

class TourResource(resources.ModelResource):
    class Meta:
        model = Tour
@admin.register(Tour)
class TourAdmin(ImportExportModelAdmin):
    resource_class = TourResource
    list_filter = ['resort']
    list_display = ['id', 'get_resort_name', 'takeoff_time', 'end_time']
    def get_resort_name(self, obj):
        return mark_safe('<a href="{0}?id={2}">{1}</a>'
                .format(reverse("admin:api_resort_changelist"), escape(obj.resort.name), escape(obj.resort.id)))
    get_resort_name.short_description = 'Resort'

