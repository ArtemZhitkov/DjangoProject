from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3  # Количество постов на странице
    ordering = ['-created_at']  # Сортировка постов по дате создания в обратном порядке

    def get_queryset(self):  # фильтрация постов по опубликованным
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):  # увеличение счетчика просмотров
        post = super().get_object()
        post.views_count += 1
        post.save()
        return post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')
    initial = {'published': True}  # дефолтное значение опубликованности


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_detail')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete_confirm.html'
    success_url = reverse_lazy('blog:post_list')
    context_object_name = 'post'
