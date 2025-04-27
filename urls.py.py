from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tabs/', views.tabs, name='tabs'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('collapsible/', views.collapsible, name='collapsible'),
    path('images/', views.images, name='images'),
    path('slider/', views.slider, name='slider'),
    path('tooltips/', views.tooltips, name='tooltips'),
    path('popups/', views.popups, name='popups'),
    path('links/', views.links, name='links'),
    path('css-properties/', views.css_properties, name='css_properties'),
    path('frames/', views.frames, name='frames'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
