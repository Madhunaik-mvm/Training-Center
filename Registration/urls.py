#from django.contrib import admin  -we dont want admin here so we commented
from django.urls import path,re_path
from Registration import views

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    #path('admin/', admin.site.urls),
]