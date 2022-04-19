from django.urls import path
from adminapp.views import IndexTemplateView, UserCreateView, UserUpdateView, UserDeleteView, UserListView, \
    CategoryListView, CategoryDeleteView, CategoryUpdateView, ProductListView, CategoryCreateView, ProductsUpdateView, \
    ProductsCreateView, ProductsDeleteView
from django.views.i18n import set_language

app_name = 'adminapp'
urlpatterns = [
    path('',IndexTemplateView.as_view(),name='index'),
    path('users/',UserListView.as_view(),name='admin_users'),
    path('user-create/',UserCreateView.as_view(),name='admin_user_create'),
    path('user-update/<int:pk>/',UserUpdateView.as_view(),name='admin_user_update'),
    path('user-delete/<int:pk>/',UserDeleteView.as_view(),name='admin_user_delete'),

    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category/create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(), name='admin_category_delete'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_category_update'),
    # path('category-detail/<int:pk>/', CategoryDetailView.as_view(), name='admin_category_detail'),

    path('product/', ProductListView.as_view(), name='admins_product'),
    path('products-update/<int:pk>/', ProductsUpdateView.as_view(), name='admins_product_update'),
    path('products-create/', ProductsCreateView.as_view(), name='admins_product_create'),
    path('products-delete/<int:pk>/', ProductsDeleteView.as_view(), name='admins_product_delete'),

    path('lang/', set_language, name='set_language'),
]
