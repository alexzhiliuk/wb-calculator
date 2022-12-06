from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        
        self.fields["first_name"].widget.attrs.update({"placeholder": "Имя"})
        self.fields["last_name"].widget.attrs.update({"placeholder": "Фамилия"})
        self.fields["email"].widget.attrs.update({"placeholder": "E-mail"})
        self.fields["password"].widget.attrs.update({
            "placeholder": "Пароль", 
            "id": "password", 
            "onchange": "changePassword()"
        })
        self.fields["password2"].widget.attrs.update({
            "placeholder": "Повторите пароль", 
            "id": "confirmPassword" , 
            "onchange": "changePassword()"
        })

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password2"]


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({
            "class": "form-control", 
        })
        self.fields["email"].label = "E-mail адрес"

        self.fields["password"].widget.attrs.update({
            "class": "form-control", 
        })
        self.fields["password"].label = "Пароль"


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "E-mail",
        }

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

