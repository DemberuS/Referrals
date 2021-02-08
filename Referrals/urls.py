from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from account.views import (
    register_view,
    login_view,
    logout_view,
    account_view,
    home_screen_view,
)

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('account/', include('account.urls', namespace='account')),
    path('admin/', admin.site.urls, name='admin'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name=
         'password_reset/password_change_done.html'), name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)