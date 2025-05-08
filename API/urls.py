# from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('products/',views.product_list),
    path('products/<int:pk>/',views.product_detail),
    # path('orders/',views.order_list),
    # path('products-info',views.product_info),
    # path('products/',views.productListView.as_view()),
    # path('products/filter/',views.productFilterview.as_view()),
    path('products/<int:productId>/',views.productRetrieveView.as_view()),
    path('products/info',views.ProductInfoView.as_view()),
    # path('products/', views.ProductListView.as_view()),
    # path('user-orders/',views.UserOrderListAPIView.as_view()),
    path('product-create/',views.ProductCreateAPIView.as_view()),
    path('products/', views.productListCreateAPIView.as_view()),

    # path('',views.home,name="home")


]

router = DefaultRouter()
router.register('orders',views.OrderViewSet)
urlpatterns += router.urls