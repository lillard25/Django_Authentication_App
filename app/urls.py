from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomPasswordResetForm

urlpatterns = [
    path("", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("forgot-password/", auth_views.PasswordResetView.as_view(
        template_name="app/forgot_password.html",
        email_template_name="app/password_reset_email.html",
        subject_template_name="app/password_reset_subject.txt",
        success_url="/forgot-password/done/",
        form_class=CustomPasswordResetForm
    ), name="forgot_password"),
    path("forgot-password/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="app/password_reset_done.html"
    ), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="app/password_reset_confirm.html"
    ), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="app/password_reset_complete.html"
    ), name="password_reset_complete"),
    path("change-password/", views.change_password_view, name="change_password"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.logout_view, name="logout"),
]
