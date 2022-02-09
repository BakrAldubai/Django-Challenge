from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index , name = 'home'),
    path('products/', views.products , name = 'all-products'),
    path('add-product/', views.add_products ,name='add-product-form'),
    path('update-product/<str:product_id>', views.update_products,name='update-product-form'),
    path('delete-product/<str:product_id>/', views.delete_products, name="delete-product-form"),
    path('brands/', views.brands, name='all-brands'),
    path('add-brand/', views.add_brands ,name='add-brand-form'),
    path('update-brand/<str:brand_id>', views.update_brands ,name='update-brand-form'),
    path('delete-brand/<str:brand_id>/', views.delete_brands, name="delete-brand-form"),
    path('brands/<slug:brand_id>',views.brand_details,name='brand-detail'),
    path('products/<slug:product_id>',views.product_details,name='product-detail'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),









]