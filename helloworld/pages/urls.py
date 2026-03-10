from django.urls import path
from .views import (
    HomePageView, AboutPageView, ContactPageView, ProductIndexView, 
    ProductShowView, ProductCreateView, ProductCreateSuccessView,
    ImageViewFactory, ImageViewNoDI
)
from .utils import ImageLocalStorage

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/create/success/', ProductCreateSuccessView.as_view(), name='product_create_success'),
    path('products/<str:id>', ProductShowView.as_view(), name='product_show'),
    
    # Imagen CON Inyección de Dependencias
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    
    # Imagen SIN Inyección de Dependencias
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenodi_index'),
    path('imagenotdi/save', ImageViewNoDI.as_view(), name='imagenodi_save'),
]