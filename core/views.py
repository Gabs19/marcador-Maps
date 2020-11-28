from django.shortcuts import render, redirect
from .models import PointerMarker
from .forms import PointerMarkerModelForm
import folium

# Create your views here.
def index(request):

    pointer_fix = (-8.3833569, -38.5757127)
    map_view = folium.Map(width = 1000, height = 500, location = pointer_fix, zoom_start = 7)

    if request.method == 'POST':
        form = PointerMarkerModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('')

    else:
        form = PointerMarkerModelForm()


    pointer = PointerMarker.objects.all()
    
    for _ in pointer:
        latitude = _.latitude
        longitude = _.longitude
        nome = _.nome_local

        folium.Marker([latitude,longitude], tooltip = 'click here more', popup = nome,icon = folium.Icon(color = 'blue', icon = 'cloud')).add_to(map_view)

    map_view = map_view._repr_html_() 

    return render(request, 'index.html', {'form' : form, 'map' : map_view})