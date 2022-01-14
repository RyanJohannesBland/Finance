from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from financialplanner.budget import views
from rest_framework_simplejwt.views import TokenObtainPairView


router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('subcategories', views.SubCategoryViewSet)
router.register('transactions', views.TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]
