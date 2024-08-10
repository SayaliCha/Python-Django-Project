"""
URL configuration for online_shopping project.

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
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view),
    #path('category_product_list', views.category_product_list),
    path('category/', views.category_view, name='category'),
    path('category/<str:category_name>',views.category_page, name='category_page'),
    path('sidebar',views.sidebar),
    path('filter/<int:pid>',views.filter_cate),
    
path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase-item-quantity/<int:item_id>/', views.increase_item_quantity, name='increase_item_quantity'),
    path('decrease-item-quantity/<int:item_id>/', views.decrease_item_quantity, name='decrease_item_quantity'),
    # other URLs

    path('order',views.order),
path('success/', views.success1, name='success'),    

]


