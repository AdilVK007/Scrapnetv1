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
    path('scrap_dealer_view_post/', views.scrap_dealer_view_post),
    path('view_rejected_scrap_dealer_post/', views.view_rejected_scrap_dealer_post),
    path('scrapped_vehicle_view_post/', views.scrapped_vehicle_view_post),
    path('view_users_post/', views.view_users_post),

    #policestation
    path('changepasspolice/', views.changepasspolice),
    path('changepass_post/', views.changepass_post),
    path('addsuspeciousactvity/', views.addsuspeciousactvity),
    path('addsuspeciousactvity_post/', views.addsuspeciousactvity_post),
    path('viewsusactivity/', views.viewsusactivity),
    path('editsusactivity/<id>', views.editsusactivity),
    path('editsusactivity_post/', views.editsusactivity_post),
    path('deletesusactity/<id>', views.deletesusactity),
    path('viewsusactivity_post/', views.viewsusactivity_post),
    path('viewscrappedvehicle/', views.viewscrappedvehicle),
    path('viewscrappedvehicle_post/', views.viewscrappedvehicle_post),
    # path('viewscrappedvehicle_post/', views.viewscrappedvehicle_post),
    path('police_home/', views.police_home),

    #RTO MODULE
    path('changepass/', views.changepass),
    path('changepass_post/', views.changepass_post),
    path('viewprofile/', views.viewprofile),
    # path('viewprofile_post/', views.viewprofile_post),
    path('vehicleadd/', views.vehicleadd),
    path('vehicleadd_post/', views.vehicleadd_post),
    path('viewveh/', views.viewveh),
    path('viewveh_post/', views.viewveh_post),
    path('editveh/<id>', views.editveh),
    path('editveh_post/', views.editveh_post),
    path('deleteveh/<id>', views.deleteveh),
    path('viewusers/', views.viewusers),
    path('viewusers_post/', views.viewusers_post),
    path('viewscrapedveh/', views.viewscrapedveh),
    path('viewscrapedveh_post/', views.viewscrapedveh_post),
    path('certificate_rto/<vid>', views.certificate_rto),
    path('certificate_rto_post/', views.certificate_rto_post),
    path('viewsusAct_rto/<vid>', views.viewsusAct_rto),
    path('viewsusActrto_post/', views.viewsusActrto_post),
    path('rto_home/', views.rto_home),

    #scrapdealer Module
    path('signup_dealer/', views.signup_dealer),
    path('signup_dealer_post/', views.signup_dealer_post),
    path('dealer_viewprofile/', views.dealer_viewprofile),
    path('updateprofile/', views.updateprofile),
    path('updateprofile_post/', views.updateprofile_post),
    path('viewrequest/', views.viewrequest),
    path('viewrequest_post/', views.viewrequest_post),
    path('viewsusAct/', views.viewsusAct),
    path('viewsusAct_post/', views.viewsusAct_post),
    path('viewverifystats/', views.viewverifystats),
    path('viewverifystats_post/', views.viewverifystats_post),
    path('scrapstationup/', views.scrapstationup),
    path('scrapstationup_post/', views.scrapstationup_post),
    path('scrapdealer_home/', views.scrapdealer_home),
    path('pending_scrapreq/', views.pending_scrapreq),
    path('viewapproved_scrapreq/', views.viewapproved_scrapreq),
    path('viewrejected_scrapreq/', views.viewrejected_scrapreq),
    path('view_userrequest_rto/', views.view_userrequest_rto),
    path('approve_user_request/<id>', views.approve_user_request),
    path('reject_user_request/<id>', views.reject_user_request),

    # user

    path('usersignup/', views.usersignup),
    path('usersignup_post/', views.usersignup_post),
    path('changepasswd/', views.changepasswd),
    path('changepasswd_post/', views.changepasswd_post),
    path('userviewprofile/', views.userviewprofile),
    path('edituserprofile/', views.edituserprofile),
    path('edituserprofile_post/', views.edituserprofile_post),
    # path('userviewprofile_post/', views.userviewprofile_post),
    path('viewvehicle/', views.viewvehicle),
    path('viewvehicle_post/', views.viewvehicle_post),
    path('userviewcertificate/<id>', views.userviewcertificate),
    # path('userviewscrapdealer/<id>', views.userviewscrapdealer),
    path('userviewscrapdealer/', views.userviewscrapdealer),
    path('userviewscrapdealer_post/', views.userviewscrapdealer_post),
    path('addscraprequest/<id>', views.addscraprequest),
    path('addscraprequest_post/<id>', views.addscraprequest_post),
    path('viewscrappingstatus/', views.viewscrappingstatus),
    path('user_home/', views.user_home),

# -------AI---------------
path('dmgpredict/', views.dmgpredict),
path('damageprediction_post/', views.damageprediction_post)
]

