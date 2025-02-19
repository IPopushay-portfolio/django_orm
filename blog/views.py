from blog.models import Blog
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, TemplateView)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.urls import reverse


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'


class BlogCreateView(CreateView):
    model = Blog
    fields = ['blog_name', 'content', 'image', 'create-at', 'publication']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.context_data['error_message'] = ''
        return response


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['blog_name', 'content', 'image', 'create-at', 'publication']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog')


class BlogContactsTemplateView(TemplateView):
    model = Blog
    fields = ['name', 'message']
    template_name = "blog/contacts.html"
