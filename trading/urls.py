from django.urls import path, include
from rest_framework import routers
from .views import PlaceOrderViewSet, TotalInvestmentViewSet

# Create a router instance
router = routers.DefaultRouter()

# Register your views with the router
router.register(r'place_order', PlaceOrderViewSet, basename='place-order')
router.register(r'total_investment', TotalInvestmentViewSet, basename='total-investment')

# Include the router's URLs in your urlpatterns
urlpatterns = router.urls
