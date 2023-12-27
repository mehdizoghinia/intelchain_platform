from django.contrib import admin

from .models import Business,Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["pkid",'id', 'name']  # Display fields in the admin list view
    search_fields = ['name']  # Add a search bar to search by name in the admin interface


class BusinessAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "business_name", "display_projects", "website", "location","phone","display_refers"]
    list_display_links = ["pkid", "id", "user"]
    list_filter = ["id", "pkid"]

    def display_projects(self, obj):
        # Fetching all related projects and joining their names into a string
        return ', '.join([project.name for project in obj.projects.all()])

    def display_refers(self, obj):
        # Fetching all related referred products and joining their names into a string
        return ', '.join([product.name for product in obj.refers.all()])

    display_projects.short_description = 'Projects'  # Set a custom header for the column
    display_refers.short_description = 'Refers to'  # Set a custom header for the column



admin.site.register(Business, BusinessAdmin)