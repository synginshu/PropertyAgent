from django.http import HttpResponse
from apps.propertyagent.models import Property
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
def index(request):
  latest_properties = Property.objects.all().order_by ("-date_added")[:5]
  return render_to_response("propertyagent/index.html", { 'latest_properties' : latest_properties }) 

def detail(request, prop_id):
  p = get_object_or_404(Property, pk=prop_id)
  return render_to_response("propertyagent/detail.html", { 'prop' : p }) 

