from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#url for the log in sessions
    url(r'^$', include('account.urls')),
    url(r'^account/', include('account.urls')),
#url for the image uploading
    url(r'^core/', include('core.urls')),
    # python-social-auth

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
