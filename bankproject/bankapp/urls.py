
from.import views
from django.urls import path
app_name='bankapp'

urlpatterns=[
    path('',views.home,name='home'),
    path('new/',views.new,name='new'),
    path('add/',views.customer_create_view,name='customer'),

    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),

]