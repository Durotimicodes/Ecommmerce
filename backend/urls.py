from django.urls import path
from .. import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('new_order/', views.new_order, name='new_order'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]