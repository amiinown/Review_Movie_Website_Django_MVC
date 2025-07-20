from django.core.exceptions import ValidationError
from .models import User
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "phone_number", "username", "is_staff")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] and cd["password2"] and cd["password1"] != cd["password2"]:
            raise ValidationError("password are not match.")
        return cd['password2']
    
    def clean_phone_number(self):
        cd = self.cleaned_data
        if len(cd["phone_number"]) != 11:
            raise ValidationError("phone should be 11 number.")
        return cd["phone_number"]
    
    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="You can change password by <a href=\'../password/\'>this form</a>.")

    class Meta:
        model = User
        fields = ("phone_number" ,"email", "username", "password", "last_login", "is_staff", "date_joined")


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label="نام کاربری", widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label="شماره همراه", max_length=11, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("این شماره یا ایمیل قبلا ثبت شده است.")
        return email
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number.isdigit() or len(phone_number) != 11:
            raise ValidationError("شماره همراه را به درستی وارد کنید.")
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValidationError("این شماره یا ایمیل قبلا ثبت شده است.")
        return phone_number


class UserRegisterVrifyCodeForm(forms.Form):
    code = forms.IntegerField(label="کد", widget=forms.NumberInput(attrs={'class':'form-class'}))

class UserLoginForm(forms.Form):

    identifier = forms.CharField(label="ایمیل یا شماره همراه", widget=forms.TextInput(attrs={'class':'form-control'}))
    password =forms.CharField(label="رمز عبور", widget=forms.PasswordInput(attrs={'class':'form-control'}))