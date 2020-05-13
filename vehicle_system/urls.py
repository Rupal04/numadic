from django.conf.urls import url
from vehicle_system import views

urlpatterns = [
        # url('geo_data', views.get_geo_data),
        url('place_interactions', views.get_vehicle_list),
        url('vehicle_activity', views.get_vehicle_activity),
    ]