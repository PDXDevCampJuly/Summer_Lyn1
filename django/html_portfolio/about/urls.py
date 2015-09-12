from django.conf.urls import include, url
from about import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='toc'),
    url(r'^_me', views.aboutme, name='AllAboutMe')
]
