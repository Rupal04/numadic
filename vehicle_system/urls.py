from django.conf.urls import url
from vehicle_system import views

urlpatterns = [
        url('place_interactions', views.get_vehicle_list),
        url('vehicle_activity', views.get_vehicle_activity),
    ]