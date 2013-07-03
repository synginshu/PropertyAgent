from django.db import models


PROPERTY_TYPES = (
    ( 'TR', 'Terrace' ),
    ( 'SD', 'Semi-Detached'),
    ( 'CD', 'Condominium'),
    ( 'SA', 'Service Apartment'),
    ( 'BG', 'Bungalow'),
    ( 'TH', 'Town-house'),
    ( 'AP', 'Apartment'))

ENCUMBERENCE = ( 
    ( 'FH', 'Freehold' ), 
    ( 'LH', 'Leasehold') )

class Area(models.Model):
  area_name = models.CharField(max_length = 50)

  def __unicode__(self):
    return self.area_name

class SubArea(models.Model):
  sub_area_name = models.CharField(max_length = 50)
  area = models.ForeignKey(Area)

  def __unicode__(self):
    return self.sub_area_name + " (" + self.area.area_name + ")"

class Agent(models.Model):
  phone_number = models.CharField(max_length = 20)
  name = models.CharField(max_length=50)
  email = models.EmailField()

  def __unicode__(self):
    return self.name 

class Amenities(models.Model):
  name = models.CharField(max_length=50)

  def __unicode__(self):
    return self.name 

  class Meta:
    verbose_name = "Amenity"
    verbose_name_plural = "Amenities"


# Create your models here.
class Property(models.Model):
  
  property_type = models.CharField(max_length = 2, choices = PROPERTY_TYPES, default="CD")
  encumberence = models.CharField(max_length = 2, choices = ENCUMBERENCE, default="FH")
  land_size = models.PositiveIntegerField(help_text="sq ft", default=0)
  built_up = models.PositiveIntegerField(help_text="sq ft", default=0)
  sub_area = models.ForeignKey(SubArea)
  bedrooms = models.PositiveSmallIntegerField(default=0)
  bathrooms = models.PositiveSmallIntegerField(default=0)
  total_sale_price = models.DecimalField(max_digits = 10, decimal_places=2, default=0)
  unit_sale_price = models.DecimalField(max_digits = 5, decimal_places=2, help_text="psf", default=0)
  total_rental_price = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
  unit_rental_price = models.DecimalField(max_digits=3,decimal_places=2, help_text="psf", default=0)
  album_link = models.URLField()
  for_sale = models.BooleanField()
  for_rent = models.BooleanField()
  agent = models.ForeignKey(Agent)
  title = models.CharField(max_length = 100)
  description = models.TextField()
  amenities = models.ManyToManyField(Amenities)
  date_added = models.DateTimeField("Date added", auto_now_add=True)

  class Meta:
    verbose_name = "Property"
    verbose_name_plural = "Properties"

  def __unicode__(self):
    return self.title + " in " + self.sub_area.sub_area_name + " (" + self.sub_area.area.area_name + ")"



