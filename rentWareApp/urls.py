from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import InventoryList

#from django.contrib import auth


urlpatterns = [

    url(r'^inventory/$', InventoryList.as_view()),
    url(r'^$', views.about, name='about'),
    url(r'^customer_list/$', views.customer_list, name='customer_list'),
    url(r'^customer_new/$', views.customer_new, name='customer_new'),
    url(r'^customer_main_view/(?P<customer_pk>\d+)$', \
            views.customer_main_view, name='customer_main_view'),
    url(r'^contact_list/(?P<customer_pk>\d+)$',
        views.contact_list, name='contact_list'),
    url(r'^contact_new/(?P<customer_pk>\d+)$',
        views.contact_new, name='contact_new'),
    url(r'^comment_list/(?P<customer_pk>\d+)$',
        views.comment_list, name='comment_list'),
    url(r'^comment_new/(?P<customer_pk>\d+)$',
        views.comment_new, name='comment_new'),

    url(r'^image_list/(?P<customer_pk>\d+)$',
        views.image_list, name='image_list'),
    url(r'^image_new/(?P<customer_pk>\d+)$', views.image_new, name='image_new'),

    url(r'^address_list/(?P<customer_pk>\d+)$',
        views.address_list, name='address_list'),
    url(r'^address_new/(?P<customer_pk>\d+)$',
        views.address_new, name='address_new'),

    url(r'^rental_list/(?P<customer_pk>\d+)$',
        views.rental_list, name='rental_list'),
    url(r'^rental_new/(?P<customer_pk>\d+)$',
        views.rental_new, name='rental_new'),


    url(r'^inventorys/$',
        views.inventory_list, name='inventory_list'),

    url(r'^flagsearch/(?P<pk>\d+)/$',
        views.flagsearch_list, name='flagsearch_list'),

    url(r'^tandc/$', views.tandc, name='tandc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
