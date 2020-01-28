from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout



urlpatterns=[
    url(r'^$',views.index,name='Index'),
    url(r'^my-profile/',views.my_profile, name='my-profile'),
    url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
    url(r'^defaulters',views.defaulterer, name='defaulters'),
    url(r'^new/defaulter$',views.new_defaulter, name='new-defaulter'), 
    url(r'^view/defaulter/(\d+)',views.view_defaulter,name='view_defaulters'),
    url(r'^business',views.businesses, name='business'),
    url(r'^notifications',views.notification, name='notifications'),
    url(r'^new/notification$',views.new_notification, name='new-notification'),
    url(r'^search/',views.search_results, name='search_results'), 
    url('', include('social_django.urls', namespace='social')),
    url('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},name='logout')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)