"""wechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from datashow.views import index, zhishui, detial, person, wxjz
from handsomelady.views import handsomelady_index
from question.views import index_question, index_guize

from dlnews.views import dlnews_index, dlnews_show,ajax_getmore

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dt/$', index),
    url(r'^ques/$',index_question),
    url(r'^guize/', index_guize),
    url(r'^zhishui/', zhishui),
    url(r'^detial/$', detial),
    url(r'^handsomelady', handsomelady_index),
    url(r'^dlnews/$', dlnews_index),
    url(r'^dlnews-show/', dlnews_show),
    url(r'^ajax-getmore/', ajax_getmore),
    url(r'^person/',person),
    url(r'^wxjz/', wxjz),
]
