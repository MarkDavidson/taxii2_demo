"""taxii2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import taxii2.views

urlpatterns = [
    url(r'^taxii/$', taxii2.views.DiscoveryView.as_view({'get': 'list'})),
    url(r'^taxii/mygroup/channels/', taxii2.views.ChannelView.as_view({'get': 'list'})),
    url(r'^taxii/mygroup/collections/', taxii2.views.ChannelView.as_view({'get': 'list'})),
    url(r'^admin/', admin.site.urls),
]
