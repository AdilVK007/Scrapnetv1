"""
URL configuration for scrapnetnew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from Myapp import views

urlpatterns = [
    path('login/',views.login),
    path('change_password/',views.change_password),
    path('rto_management/',views.rto_management),
    path('rto_view/',views.rto_view),
    path('editrto/<id>', views.editrto),
    path('deleterto/<id>',views.deleterto),
    path('police_station/',views.police_station),
    path('police_station_view/',views.police_station_view),
    path('editpolicestation/<id>', views.editpolicestation),
    path('deletepolicestation/<id>', views.deletepolicestation),
    path('scrapdealer/<id>', views.scrapdealer),
    path('scrap_dealer_approve/',views.scrap_dealer_approve),
    path('rejectscrapdealer/<id>', views.rejectscrapdealer),
    path('viewapprovedscrapdealer/',views.viewapprovedscrapdealer),
    path('scrap_dealer_view/',views.scrap_dealer_view),
    path('view_rejected_scrap_dealer/',views.view_rejected_scrap_dealer),
    path('scrapped_vehicle_view/',views.scrapped_vehicle_view),
    path('view_users/',views.view_users),
    path('admin_home/',views.admin_home),
    path('login_post/',views.login_post),
    path('change_pass_post/', views.change_pass_post),
    path('rto_management_post/', views.rto_management_post),
    path('rtoview_post/',views.rtoview_post),
    path('editro_post/', views.editro_post),
    path('policestation_post/',views.policestation_post),
    path('policestationview_post/', views.policestationview_post),
    path('editpolicestation_post/', views.editpolicestation_post),
    path('scrap_dealer_approve_post/',views.scrap_dealer_approve_post),
    path('viewapprovedscrapdealer_post/', views.viewapprovedscrapdealer_post),
    path('viewapprovedscrapdealer_post/', views.viewapprovedscrapdealer_post),
    path('view_rejected_scrap_dealer_post/', views.view_rejected_scrap_dealer_post),
    path('scrapped_vehicle_view_post/', views.scrapped_vehicle_view_post),
    path('view_users_post/', views.view_users_post)
]
