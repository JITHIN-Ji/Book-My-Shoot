from django.urls import path
from .import views

urlpatterns=[

    path('logins',views.logins,name='logins'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('',views.index,name='index'),
    path('userreg',views.userreg,name='userreg'),
    path('userhome',views.user_home,name='userhome'),
    path('profile',views.up_profile,name='profile'),
    path('viewuser',views.admin_view_user,name='viewuser'),
    path('category',views.admin_category,name='category'),
    path('adminservice',views.adm_service,name='service'),
    path('updatecategory/<id>',views.update_catagory,name='updatecategory'),
    path('deletecategory/<id>',views.delete_category,name='deletecategory'),
    path('updateservice/<id>',views.update_service,name='updateservice'),
    path('deleteservice/<id>',views.delete_service,name='deleteservice'),
    path('userviewservice',views.user_view_service,name='userviewservice'),
    path('userbooking/<id>',views.user_booking,name='userbooking'),
    path('adminviewbooking',views.admin_view_booking,name='adminviewbooking'),
    path('adm_accept_booking/<id>',views.adm_accept_booking,name='adm_accept_booking'),
    path('adm_reject_booking/<id>',views.adm_delete_booking,name='adm_reject_booking'),
    path('user_view_booking',views.user_view_booking,name='user_view_booking'),
    path('user_payment/<id>',views.user_payment,name='user_payment'),
    path('adm_view_advance_payment/<id>',views.adm_view_advance_payment,name='adm_view_advance_payment'),
    path('admin_advance_payment/<id>',views.admin_advance_payment,name='admin_advance_payment'),
    path('userfullpayment/<id>',views.userfullpayment,name='userfullpayment'),
    path('feedbacks',views.feedbacks,name='feedbacks'),
    path('admin_upload_video/<id>',views.admin_upload_video,name='admin_upload_video'),
    path('admin_work',views.admin_work,name='admin_work'),
    path('admin_view_feedback',views.admin_view_feedback,name='admin_view_feedback'),
    path('user_view_upload_file/<id>',views.user_view_upload_file,name='user_view_upload_file'),
    
    




]