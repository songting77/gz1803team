from django.conf.urls import url

from t8 import views


urlpatterns = [
    url(r'^index$',views.index),
    url(r'^send_my_email$',views.send_my_email),
    url(r'^send_my_email_v1$',views.send_my_email_v1),
    url(r'^verify$',views.verify),
    url(r'^active$',views.active),
    url(r'^send_many_email',views.send_many_email),
    # url(r'^test_log',views.test_log)
]