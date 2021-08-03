from django.urls import path
from . import views
urlpatterns = [
    path('articals',views.viewarticals,name="articals"),
]