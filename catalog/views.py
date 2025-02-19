from catalog.models import Product
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, TemplateView)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.urls import reverse


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = ['prod_name', 'category', 'description', 'image', 'price']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.context_data['error_message'] = ''
        return response


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['prod_name', 'category', 'description', 'image', 'price']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/confirm_delete.html'
    success_url = reverse_lazy('catalog:home')


class ContactsTemplateView(TemplateView):
    model = Product
    fields = ['name', 'message']
    template_name = "catalog/contacts.html"
