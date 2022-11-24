from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


import folium
import geocoder
from folium import plugins

g = geocoder.ip('me')

# Create your views here.
# def home(request) :
#     # map = folium.Map(location=[37.7854, 128.4698],zoom_start=15, width='100%', height='100%',)
#     map = folium.Map(location=g.latlng,zoom_start=15, width='100%', height='100%',)
#     maps=map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 

#     return render(request, 'home.html',{'map' : maps})


m = folium.Map([45, 3], zoom_start=4)

plugins.ScrollZoomToggler().add_to(m)

from django.shortcuts import render
from folium import plugins
import folium
import geocoder     #import geojson

g = geocoder.ip('me')   #현재 내위치
# Create your views here.
def home(request) :
    map = folium.Map(location=g.latlng,zoom_start=15, width='100%', height='100%',)
    plugins.LocateControl().add_to(map)
    plugins.Geocoder().add_to(map)

    maps=map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 (folium)

    return render(request,'blog/home.html',{'map' : maps})