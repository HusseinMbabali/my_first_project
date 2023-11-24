"""
URL configuration for real_estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from realestate.views import edit_title_view, edit_customer_view, edit_estate_view, edit_house_view, edit_land_view, edit_payment_view, index_view, realestate_list_view, add_estate_view, add_land_view, add_house_view, add_customer_view, add_payment_view, add_title_view, delete_estate_view, delete_land_view, delete_house_view, delete_customer_view, delete_payment_view, delete_title_view,sign_up_view, getestates, gethouses, getlands, getcustomers, getpayments, gettitles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index_page'),
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('realestate_list/', realestate_list_view, name='realestate_list_page'),
    path("estates/", getestates),
    path("houses/", gethouses),
    path("lands/", getlands),
    path("customers/", getcustomers),
    path("payments/", getpayments),
    path("title/", gettitles),

#add    
    path('add_estate/', add_estate_view, name='add_estate_page'),
    path('add_land/', add_land_view, name='add_land_page'),
    path('add_house/', add_house_view, name='add_house_page'),
    path('add_customer/', add_customer_view, name='add_customer_page'),
    path('add_payment/', add_payment_view, name='add_payment_page'),
    path('add_title/', add_title_view, name='add_title_page'),

#edit    
    path('edit_estate/<int:estate_id>/', edit_estate_view, name='edit_estate_page'),
    path('edit_land/<int:land_id>/', edit_land_view, name='edit_land_page'),
    path('edit_house/<int:house_id>/', edit_house_view, name='edit_house_page'),
    path('edit_customer/<int:customer_id>/', edit_customer_view, name='edit_customer_page'),
    path('edit_payment/<int:payment_id>/', edit_payment_view, name='edit_payment_page'),
    path('edit_title/<int:title_id>/', edit_title_view, name='edit_title_page'),

#delete    
    path('delete_estate/<int:estate_id>/', delete_estate_view, name='delete_estate_page'),
    path('delete_land/<int:land_id>/', delete_land_view, name='delete_land_page'),
    path('delete_house/<int:house_id>/', delete_house_view, name='delete_house_page'),
    path('delete_customer/<int:customer_id>/', delete_customer_view, name='delete_customer_page'),
    path('delete_payment/<int:payment_id>/', delete_payment_view, name='delete_payment_page'),
    path('delete_title/<int:title_id>/', delete_title_view, name='delete_title_page'),
]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)