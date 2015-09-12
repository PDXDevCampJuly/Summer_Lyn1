from django.conf.urls import include, url
from zen_mockup import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^mockup', views.zen_mockery(), name='zen_mockery'),
]