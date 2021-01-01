from django.urls import path
from dashboard import views
from dashboard.views import charts_dash
#from dashboard.views import BarChartview

urlpatterns = [
    path('', views.home,),
    path('blank', views.blank_dash),
    path('buttons', views.buttons_dash),
    path('cards', views.cards_dash),
    path('charts', views.charts_dash),
    path('forgot-password', views.forgot_password),
    path('404', views.error_404),
    path('login_dash', views.login_dash),
    path('tables', views.tables_dash),
    path('utilities-animation', views.utilities_animation),
    path('utilities-border', views.utilities_border),
    path('utilities-color', views.utilities_color),
    path('utilities-other', views.utilities_other),
    path('register', views.register),
    path('choose', views.upload),
    path('badrecords_dash',views.badrecords_dash),
    path('manageteam_dash',views.manageteam_dash), 
    path('display_mandate',views.display_mandate),
    path('upload_candidate',views.upload_candidate),
    path('display_candidate',views.display_candidate),
    path('mandate_choose',views.mandate_upload),
    path('upload_mandate',views.upload_mandate),
    path('display_mandate',views.display_mandate),
    #path('charts',BarChartview.as_view()),
    path('mandate_table',views.Mandate_table),
    


    #path('mandate_import_data', views.mandate_import_data),
    #path('mandate_fieldmatching', views.mandate_fieldmatching),
    #path('mandate_choose', views.mandate_choose),
    #path('mandate_import_p', views.mandate_import_data_p),
    
    


]
