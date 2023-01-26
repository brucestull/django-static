"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from config.settings.common import THE_SITE_NAME, STATIC_URL
from config.settings.development import STATIC_ROOT

urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name="home.html",
            extra_context={'the_site_name': THE_SITE_NAME},
        ),
        name='home',
    ),

    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# It seems that these print statements are only run on server restart.
# In development, `settings.DEBUG` is defined in `config\settings\development.py`. And this `settings.DEBUG` reflects that value.
# So, if we change the DEBUG setting, we may need to restart the server?
print('')
print('settings.DEBUG: ', settings.DEBUG)
print('')

if settings.DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

# static(MEDIA_URL, document_root = MEDIA_ROOT)