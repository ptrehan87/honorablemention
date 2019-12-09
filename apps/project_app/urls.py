from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^log_reg$', views.log_reg),
    url(r'^dash$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^place_add$', views.place_add),
    url(r'^view_place/(?P<place_id>\d+)$', views.view_place),
    url(r'^delete/(?P<place_id>\d+)$', views.delete),
    url(r'^edit/(?P<place_id>\d+)$', views.edit),
    url(r'^place_edit/(?P<place_id>\d+)$', views.place_edit),
    url(r'^add_cat$', views.add_cat),
    url(r'^map/(?P<place_id>\d+)$', views.maplocation),
    url(r'^map$', views.map),
]