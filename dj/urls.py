from django.urls import path
from . import views

urlpatterns = [
    path('', views.ocn, name='ocn'),
    path('', views.ocn, name='Основа'),
    path('stixi/', views.stixi, name='stixi'),
    path('st5/', views.st5, name='st5'),
    path('lec/', views.lec, name='lec'),
    path('open/', views.open, name='open'),
    path('love/', views.love, name='love'),
    path('open2/', views.open2, name='open2'),
    path('fil/', views.fil, name='fil'),
    path('open3/', views.open3, name='open3'),
    path('grazhd/', views.grazhd, name='grazhd'),
    path('form/', views.index, name='index'),
    path('stih_form/', views.stih_form, name='stih_form'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/', views.my_profile, name='my_profile'),
    path("entry/<int:pk>",views.EntryListView.as_view(),name="dd")
]
