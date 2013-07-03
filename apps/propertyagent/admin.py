from apps.propertyagent.models import Property, Area, SubArea, Amenities, Agent
from django.contrib import admin


class PropertyAdmin(admin.ModelAdmin):
  # fields = [ 'area', 'sub_area', 'property_type', 'encumberence', 'land_size' ]
  fieldsets = [
    ('Description',{'fields':['title', 'description']}),
    ('Address',{'fields':['sub_area']}),
    ('Details',{'fields':[
      'property_type', 
      'encumberence', 
      'land_size', 
      'built_up', 
      'bedrooms',
      'bathrooms',
      'amenities',
      'for_sale', 
      'for_rent',
      'album_link',
 ], 'classes':['collapse']}),
    ('Cost',{'fields':[
      'agent', 
      'total_sale_price', 
      'unit_sale_price', 
      'total_rental_price', 
      'unit_rental_price' ],'classes':['collapse']}),
  ] 
  list_display = ['title', 'sub_area', 'date_added' ]
  search_fields = ['title', 'sub_area__sub_area_name', 'sub_area__area__area_name', 'property_type' ]

admin.site.register(Property,PropertyAdmin)
admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(Amenities)
admin.site.register(Agent)
