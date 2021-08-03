from django.urls import path
from . import views
urlpatterns = [
    path('teams',views.showteam,name="team"),
]