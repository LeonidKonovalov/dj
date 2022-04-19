from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryUpdateFormAdmin
from adminapp.models import ProductsForm
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, TemplateView, CreateView
from mainapp.models import Product, ProductCategories
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin

# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request,'adminapp/admin.html')

class IndexTemplateView(TemplateView,BaseClassContextMixin,CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главня страница'

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return  super(IndexTemplateView, self).dispatch(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(IndexTemplateView, self).get_context_data(**kwargs)
    #     context['title'] = 'Главня страница'
    #     return context

class UserListView(ListView,BaseClassContextMixin,CustomDispatchMixin,UserDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title =  'Админка | Пользователи'
    context_object_name = 'users'

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#
#     context = {
#         'title' : 'Админка | Пользователи',
#         'users':User.objects.all()
#     }
#     return render(request,'adminapp/admin-users-read.html',context)\

class UserCreateView(CreateView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title ='Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')

    # def post(self, request, *args, **kwargs):
    #     pass
    # def get(self, request, *args, **kwargs):
    #     pass
    # def get_context_data(self, request, *args, **kwargs):
    #     pass
    # or mixin
# @user_passes_test(lambda u: u.is_superuser)
# def admin_products(request):
#
#     context = {
#         'title' : 'Админка | Продукты',
#         'users':Product.objects.all()
#     }
#     return render(request,'adminapp/admin-users-read.html',context)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):
#
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'Админка | Регистрация',
#         'form':form
#     }
#
    #
    #
    # return render(request,'adminapp/admin-users-create.html',context)
class UserUpdateView(UpdateView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title ='Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request,id):
#     user_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST,instance=user_select,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#     context = {
#          'title': 'Админка | Обновление пользователя',
#          'form':form,
#          'user_select':user_select
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request,id):
#     user = User.objects.get(id=id)
#     # user = User.objects.get(id=id).delete()
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_users'))

class UserDeleteView(DeleteView,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# Category
class CategoryListView(ListView,BaseClassContextMixin,CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-read.html'
    title = 'Админка | Список категорий'


    def get_queryset(self):
        if self.kwargs:
           return ProductCategories.objects.filter(id=self.kwargs.get('pk'))
        else:
           return ProductCategories.objects.all()

class CategoryDeleteView(DeleteView,BaseClassContextMixin,CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class CategoryUpdateView(UpdateView,BaseClassContextMixin,CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-update-delete.html'
    form_class = CategoryUpdateFormAdmin
    title = 'Админка | Обновления категории'
    success_url = reverse_lazy('admins:admin_category')

class CategoryCreateView(CreateView,BaseClassContextMixin,CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-create.html'
    success_url = reverse_lazy('admins:admin_category')
    form_class = CategoryUpdateFormAdmin
    title = 'Админка | Создание категории'

# Product
class ProductListView(ListView,BaseClassContextMixin,CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-read.html'
    title = 'Админка | Обновления категории'

class ProductsUpdateView(UpdateView, BaseClassContextMixin,CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProductsForm
    title = 'Админка | Обновление продукта'
    success_url = reverse_lazy('admins:admins_product')

class ProductsCreateView(CreateView, BaseClassContextMixin,CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = ProductsForm
    title = 'Админка | Создание продукта'
    success_url = reverse_lazy('admins:admins_product')

class ProductsDeleteView(DeleteView, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-read.html'
    success_url = reverse_lazy('admins:admins_product')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())