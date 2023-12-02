from django.urls import path
from ciesse.views import SiteListView
from ciesse.login import CustomLoginView
from ciesse.logout import logout_view
from ciesse.registration import registration_view
from ciesse.monitoring import monitoring_details
from ciesse.sitelist import sitelist_details

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="views_login"),
    path("", CustomLoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", registration_view, name="registration"),
    path("monitoring/<int:siteId>/", monitoring_details, name="monitoring"),
    path("site-list/", sitelist_details, name="site-list")
]