from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import models
from mainapp.models import ProductCategories, Product
from authapp.models import User


class UserAdminRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1','password2','last_name','first_name','email','image','age')

    def __init__(self,*args,**kwargs):
        super(UserAdminRegisterForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ведите фамилию'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фотографию'
        self.fields['age'].widget.attrs['placeholder'] = 'Возраст'


        for filed_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'



class UserAdminProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username','last_name','first_name','email','image','age')

    def __init__(self,*args,**kwargs):
        super(UserAdminProfileForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for filed_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


# class ProductAdminReadForm(UserChangeForm):
#
#     class Meta:
#         model = User
#         fields = ('username','last_name','first_name','email','image','age')
#
#     def __init__(self,*args,**kwargs):
#         super(UserAdminProfileForm, self).__init__(*args,**kwargs)
#         self.fields['username'].widget.attrs['readonly'] = True
#         self.fields['email'].widget.attrs['readonly'] = True
#
#         for filed_name , field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control py-4'
#         self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class ProductCategoriesAdminRead(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CategoryUpdateFormAdmin(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput())
    # description = forms.CharField(widget=forms.TextInput(), required=False)
    # # is_active = forms.BooleanField(widget=forms.CheckboxInput())


    class Meta:
        model = ProductCategories
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryUpdateFormAdmin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class ProductsForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=ProductCategories.objects.all())
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'category':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class ProductUpdate(ProductsForm):
    category = forms.ModelChoiceField(queryset=ProductCategories.objects.all().select_related(),
                                      empty_label=None)
    image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'category':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'