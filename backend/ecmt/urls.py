"""
URL configuration for ecmt project.

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from customer.views import CustomersViewSet
from educational_programs.views import ProgramCategoriesViewSet, ProgramSubCategoriesViewSet
from schedule.views import SchedulesViewSet, LectureViewSet
from teacher.views import WorkloadViewSet, TeacherViewSet

from .resources import ResourcesView

router = DefaultRouter()

router.register(r'customer', CustomersViewSet)
router.register(r'program_categories', ProgramCategoriesViewSet)
router.register(r'program_sub_categories', ProgramSubCategoriesViewSet)
router.register(r'schedule', SchedulesViewSet)
router.register(r'lecture', LectureViewSet)
router.register(r'workload', WorkloadViewSet)
router.register(r'teacher', TeacherViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/0/', include(router.urls)),
    path('api/0/resources/', ResourcesView.as_view()),
    path('api/0/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/0/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/0/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/0/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('__debug__/', include('debug_toolbar.urls')),
]
