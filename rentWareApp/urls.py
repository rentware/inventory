from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
#from django.contrib import auth



urlpatterns = [
#class sample

#    url(r'^pages/', include('breadcrumbs.urls')),

    url(r'^$', views.about, name='about'),

#    url(r'^test/$', views.test, name='test'),

#    url(r'^test2/$', views.test2, name='test2'),

#    url(r'^denied/$', views.denied, name='denied'),
#test for breadcrumbs
    url(r'^customer_list/$', views.customer_list, name='customer_list'),
    url(r'^customer_new/$', views.customer_new, name='customer_new'),
#    url(r'^sub_user/(?P<est_pk>\d+)/new/$', views.sub_user_new, name='sub_user_new'),

    url(r'^contact_list/(?P<customer_pk>\d+)$', views.contact_list, name='contact_list'),
    url(r'^contact_new/(?P<customer_pk>\d+)$', views.contact_new, name='contact_new'),

    url(r'^comment_list/(?P<customer_pk>\d+)$', views.comment_list, name='comment_list'),
    url(r'^comment_new/(?P<customer_pk>\d+)$', views.comment_new, name='comment_new'),

    url(r'^image_list/(?P<customer_pk>\d+)$', views.image_list, name='image_list'),
    url(r'^image_new/(?P<customer_pk>\d+)$', views.image_new, name='image_new'),

    url(r'^address_list/(?P<customer_pk>\d+)$', views.address_list, name='address_list'),
    url(r'^address_new/(?P<customer_pk>\d+)$', views.address_new, name='address_new'),

    url(r'^rental_list/(?P<customer_pk>\d+)$', views.rental_list, name='rental_list'),
    url(r'^rental_new/(?P<customer_pk>\d+)$', views.rental_new, name='rental_new'),

#    url(r'^sub_user_delete/(?P<sub_user_pk>\d+)/estab/(?P<est_pk>\d+)/$',
#    views.sub_user_delete, name='sub_user_delete'),

    url(r'^inventorys/$',
    views.inventory_list, name='inventory_list'),

    url(r'^flagsearch/(?P<pk>\d+)/$',
    views.flagsearch_list, name='flagsearch_list'),

#    url(r'^listguestflag/(?P<guest_pk>\d+)/estab/(?P<est_pk>\d+)/$',
#    views.list_guest_flag, name='list_guest_flag'),

#list_guest_flag

#    url(r'^inventory_detail/(?P<pk>\d+)/$',
#    views.inventory_detail, name='inventory_detail'),

#    url(r'^inventory_detail_administration/(?P<pk>\d+)/$',
#    views.inventory_detail_administration, name='inventory_detail_administration'),

#    url(r'^inventory_detail_contractors/(?P<pk>\d+)/$',
#    views.inventory_detail_contractors, name='inventory_detail_contractors'),

#    url(r'^inventory_detail_guests/(?P<pk>\d+)/$',
#    views.inventory_detail_guests, name='inventory_detail_guests'),

#    url(r'^inventory_detail_employees/(?P<pk>\d+)/$',
#    views.inventory_detail_employees, name='inventory_detail_employees'),

    url(r'^about/$', views.about, name='about'),
    url(r'^tandc/$', views.tandc, name='tandc'),
#    url(r'^offenses/$', views.offenses, name='offenses'),
#    url(r'^guest/(?P<est_pk>\d+)/new/$', views.guest_new, name='guest_new'),

#    url(r'^guest/(?P<pk>\d+)/edit/(?P<est_pk>\d+)/$',
#    views.guest_edit, name='guest_edit'),

#    url(r'^guest/(?P<pk>\d+)/flag/(?P<est_pk>\d+)/$',
#    views.guest_flag, name='guest_flag'),

#    url(r'^guest/(?P<guest_pk>\d+)/guest_upload_list/(?P<est_pk>\d+)/$',
#    views.guest_upload_list, name='guest_upload_list'),

#    url(r'^guest/(?P<guest_pk>\d+)/guest_visit_list/(?P<est_pk>\d+)/$',
#    views.guest_visit_list, name='guest_visit_list'),

#    url(r'^new_guest_visit/(?P<guest_pk>\d+)/inventory/(?P<est_pk>\d+)/$',
#    views.new_guest_visit, name='new_guest_visit'),

#    url(r'^edit_guest_visit/(?P<guest_pk>\d+)/(?P<visit_pk>\d+)/inventory/(?P<est_pk>\d+)/$',
#    views.edit_guest_visit, name='edit_guest_visit'),

#    url(r'^guest/(?P<guest_pk>\d+)/guest_upload_file/(?P<est_pk>\d+)/$',
#    views.guest_upload_file, name='guest_upload_file'),

#    url(r'^contractor/(?P<pk>\d+)/flag/(?P<est_pk>\d+)/$',
#    views.contractor_flag, name='contractor_flag'),

#    url(r'^employee/(?P<pk>\d+)/flag/(?P<est_pk>\d+)/$',
#    views.employee_flag, name='employee_flag'),

#    url(r'^contractor/(?P<est_pk>\d+)/new/$',
#    views.contractor_new, name='contractor_new'),
#    url(r'^contractor/(?P<pk>\d+)/edit/(?P<est_pk>\d+)/$',
#    views.contractor_edit, name='contractor_edit'),
#    url(r'^employee/(?P<est_pk>\d+)/new/$',
#    views.employee_new, name='employee_new'),
#    url(r'^employee/(?P<pk>\d+)/edit/(?P<est_pk>\d+)/$',
#    views.employee_edit, name='employee_edit'),

#    url(r'^testmethod/$', views.testmethod, name='testmethod'),

#    url(r'^hello/$', views.hello, name='hello'),

#    url(r'^checkid/(?P<SAID>\d+)/$',
#    views.check_sa_id_for_flag, name='check_sa_id_for_flag'),

#    url(r'^visit/(?P<est_pk>\d+)/new/$', views.visit_new, name='visit_new'),
#    url(r'^visit/(?P<pk>\d+)/edit/(?P<est_pk>\d+)/$',
#    views.visit_edit, name='visit_edit'),
#    url(r'^inventory_new/$',
#    views.inventory_new, name='inventory_new'),
#    url(r'^inventory/(?P<pk>\d+)/edit/$',
#    views.inventory_edit, name='inventory_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
