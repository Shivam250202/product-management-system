from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('api/', views.ProductListCreateAPI.as_view(), name='api-list-create'),
    path('api/<int:pk>/', views.ProductRetrieveUpdateDestroyAPI.as_view(), name='api-detail'),
]