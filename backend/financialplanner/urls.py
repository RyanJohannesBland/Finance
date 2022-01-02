from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from financialplanner.budget import views


router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('subcategories', views.SubCategoryViewSet)
router.register('transactions', views.TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
