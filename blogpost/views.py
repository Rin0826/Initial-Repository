from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from .models import BlogModel, Review
from django.utils import timezone

class SubscView(DetailView):
    template_name = 'blogpost/subsc.html'
    model = BlogModel

class BlogList(ListView):
    template_name = 'blogpost/list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'blogpost/detail.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogCreate(CreateView):
    template_name = 'blogpost/create.html'
    model = BlogModel
    fields = ('title', 'content', 'category', 'photo')
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    template_name = 'blogpost/delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    template_name = 'blogpost/update.html'
    model = BlogModel
    fields = {'title', 'content', 'category', 'photo'}
    success_url = reverse_lazy('list')

class BlogSubsc(SubscView):
    template_name = 'blogpost/subsc.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogReview(CreateView):
    template_name = 'blogpost/review.html'
    model = Review
    fields = ['blog', 'title', 'text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = BlogModel.objects.get(pk=self.kwargs['pk'])
        context['current_time'] = timezone.now()
        return context
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.blog.id})

def like_view(request, pk):
    post = get_object_or_404(BlogModel, pk=pk)
    post.likes += 1
    post.save()
    return redirect('detail', pk=pk)

def dislike_view(request, pk):
    post = get_object_or_404(BlogModel, pk=pk)
    post.dislikes += 1
    post.save()
    return redirect('detail', pk=pk)