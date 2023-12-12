from django.views.generic import RedirectView

from shop import views
from django.urls import path

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='store'), name='redirect-to-store'),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name='update-item'),
    path('process_order/', views.processOrder, name='process-order'),
    path('create_user/', views.CreateUser.as_view(), name='create-user')
]