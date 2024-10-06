from django.contrib import admin
from .models import Dog, Breed

class DogAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy')
    
    # Add search functionality for specific fields
    search_fields = ('name', 'breed')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('age', 'breed', 'color')

    # Define which fields can be clicked to view the details page
    list_display_links = ('name', )

    # Define how fields are displayed when editing a Dog instance
    dogfields = ('name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy')

class BreedAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'size', 'friendliness', 'trainability', 'shedding', 'exercise')
    
    # Add search functionality for specific fields
    search_fields = ('name',)

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('size', 'friendliness', 'trainability', 'shedding', 'exercise')

    # Define which fields can be clicked to view the details page
    list_display_links = ('name', )

    # Define how fields are displayed when editing a Dog instance
    dogfields = ('name', 'size', 'friendliness', 'trainability', 'shedding', 'exercise')

# Register the model and admin class
admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)