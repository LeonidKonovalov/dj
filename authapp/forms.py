from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
#from authapp.forms import UserRegisterForm, UserProfilerForm
from authapp.models import User
from mainapp.models import ProductCategories, Product

class UserLoginForm(AuthenticationForm):

    # username = forms.CharField(widget=forms.TextInput(),validators=[validate_name])
    class Meta:
        model = User
        fields = ('username','password')



    def __init__(self,*args,**kwargs):
        super(UserLoginForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class UserRegisterForm(UserCreationForm):
    # username = forms.CharField()

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

    def __init__(self,*args,**kwargs):
        super(UserRegisterForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл.почты'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите  имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите  фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserProfileForm(UserChangeForm):
    # first_name = forms.CharField(widget=forms.TextInput(),validators=[validate_name])
    image = forms.ImageField(widget=forms.FileInput(),required=False)
    age = forms.IntegerField(widget=forms.NumberInput(), required=False)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','image','age')

    def __init__(self,*args,**kwargs):
        super(UserProfileForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['username'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

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