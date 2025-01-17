"""
URL configuration for API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Accounts.routes import account_router
from Colleges.routes import college_router
from Accounts.token import CustomTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from .router import email_verification_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(account_router.urls)),
    path('api/',include(college_router.urls)),
    path('api/token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/', include(email_verification_router.urls)),


] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT) 
