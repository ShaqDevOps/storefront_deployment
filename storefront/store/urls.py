from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

# store/urls.py

app_name = 'store'



router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')
products_router.register('images', views.ProductImageViewSet, basename='product-images')


carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# urlpatterns =[
#     path('products_page', views.\)
# ]

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls

urlpatterns += [
    path('products/products_page/', views.ProductViewSet.as_view({'get': 'store/products_page'}), name='products_page'),
]