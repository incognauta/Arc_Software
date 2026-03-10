from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView
from django.urls import reverse
from django import forms
from django.contrib import messages
from .models import Product, Comment
from .utils import ImageLocalStorage

# Create your views here.
def ImageViewFactory(image_storage):
    class ImageView(View):
        template_name = 'images/index.html'
        def get(self, request):
            image_url = request.session.get('image_url', '')
            return render(request, self.template_name, {'image_url': image_url})
        def post(self, request):
            image_url = image_storage.store(request)
            request.session['image_url'] = image_url
            return redirect('image_index')
    return ImageView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "email": "chotacabra.edu.co",
            "address": "chupamestepenco University, Medellín, Colombia",
            "phone": "+57 300 666 6666",
        })
        return context

class ProductIndexView(View):
    
    template_name = 'products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.objects.all()
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'
    
    def get(self, request, id):
        try:
            viewData = {}
            product = get_object_or_404(Product, pk=id)
            viewData["title"] = product.name + " - Online Store"
            viewData["subtitle"] = product.name + " - Product information"
            viewData["product"] = product
            viewData["comments"] = product.comment_set.all()
            viewData["comment_form"] = CommentForm()
            return render(request, self.template_name, viewData)
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse('home'))
    
    def post(self, request, id):
        try:
            product = get_object_or_404(Product, pk=id)
            form = CommentForm(request.POST)
            
            if form.is_valid():
                comment = form.save(commit=False)
                comment.product = product
                comment.save()
                messages.success(request, 'Comment added successfully!')
            else:
                messages.error(request, 'Error adding comment. Please try again.')
            
            return HttpResponseRedirect(reverse('product_show', args=[id]))
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse('home'))
        
class High_price_product_index_view(View):
    template_name = 'products/high_price_index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "High price products - Online Store"
        viewData["subtitle"] = "List of high price products"
        viewData["products"] = Product.objects.filter(price__gt=5000000)
        return render(request, self.template_name, viewData)

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products' # This will allow you to loop through 'products' in your template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Products - Online Store'
        context['subtitle'] = 'List of products'
        return context 

class ProductForm(forms.ModelForm): 
    class Meta: 
        model = Product 
        fields = ['name', 'price', 'description']
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative")
        return price


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...'
            })
        }
        labels = {
            'description': 'Your Comment'
        }

class ProductCreateView(View):
    template_name = 'products/create.html'
    
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return HttpResponseRedirect(reverse('index'))
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class ProductCreateSuccessView(TemplateView):
    """Dummy view for URL config compatibility"""
    template_name = 'products/index.html'


# ============================================
# SAME APPLICATION WITHOUT DEPENDENCY INVERSION
# ============================================
class ImageViewNoDI(View):
    """Vista sin uso de Inyección de Dependencias (crear la dependencia internamente)"""
    template_name = 'imagesnotdi/index.html'
    
    def get(self, request):
        image_url = request.session.get('image_url', '')
        return render(request, self.template_name, {'image_url': image_url})
    
    def post(self, request):
        # ❌ PROBLEMA: La vista crea directamente la dependencia
        # No es flexible ni testeable
        image_storage = ImageLocalStorage()
        image_url = image_storage.store(request)
        request.session['image_url'] = image_url
        return redirect('imagenodi_index')