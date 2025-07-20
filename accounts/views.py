from django.shortcuts import render, redirect
from django.views import View
from .models import OptCode, User
from utils import send_otp_code
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, UserRegisterVrifyCodeForm
import random
from django.contrib.auth import login, authenticate, logout, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.urls import reverse_lazy

class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "از قبل وارد حساب کاربری شده اید.", "info")
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data["phone_number"], random_code)
            OptCode.objects.create(phone_number= cd["phone_number"], code= random_code)
            request.session["user_registration_info"] = {
                "phone_number": form.cleaned_data["phone_number"],
                "email": form.cleaned_data["email"],
                "username": form.cleaned_data["username"],
                "password": form.cleaned_data["password"],
            }
            messages.success(request, "کد اهراز هویت به شماره شما ارسال شد.", "success")
            return redirect("accounts:verify")
        return render(request, self.template_name, {"form":form})

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = "accounts/login.html"

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get("next")
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "از قبل وارد حساب کاربری شده اید.", "info")
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['identifier'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد حساب کاربری شدید.', 'success')
                if self.next:
                    return redirect(self.next)
                else:
                    return redirect('home:home')
        messages.error(request, 'ایمیل یا شماره تلفن یا رمز عبور اشتباه است.', 'warning')
        return render(request, self.template_name, {'form':form})

    
class UserLogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        messages.success(request, "با موفقیت از حساب کاربری خود خارج شدید.", "success")
        return redirect('home:home')
    

class UserRegisterVerifyCodeView(View):
    form_class = UserRegisterVrifyCodeForm
    template_name = 'accounts/verify.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        user_session = request.session["user_registration_info"]
        code_instance = OptCode.objects.get(phone_number=user_session["phone_number"])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            expiration_time = datetime.timedelta(minutes=2)
            expired = datetime.datetime.now() - code_instance.created > expiration_time
            if cd["code"] == code_instance.code and not expired:
                User.objects.create_user(user_session["phone_number"], user_session["email"],
                                          user_session["username"], user_session["password"])
                
                code_instance.delete()
                messages.success(request, "حساب کاربری شما با موفقیت ساخته شد.", "success")
                return redirect("home:home")
            else:
                messages.error(request, "کد وارد شده اشتباه است. دوباره تلاش نمایید", "warning")
                return redirect("accounts:verify_code")
        return redirect("home:home")
    
class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = "accounts/password_reset_form.html"
    success_url = reverse_lazy("accounts:password_reset_done")
    email_template_name = "accounts/password_reset_email.html"

class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")

class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


