from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^$', views.home, name='home'),
    #url for uploading my image
    url(r'^form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^admin/', admin.site.urls),
    url(r'^crowdsourcing/$', views.crowdsourcing, name='crowdsourcing'),
    #url for deleting images that i uploaded
    url(r'^document/delete/?(?P<pk>\d+)?/?$',views.delete_document, name='delete_document'),
    ]
