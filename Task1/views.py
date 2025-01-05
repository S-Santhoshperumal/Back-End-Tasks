from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Post
from .forms import PostForm,EditForm
# def home(request):
#     return render(request, 'posts/mainPage.html',{} )

class HomeView(ListView):
    model = Post
    template_name = 'Task1/main.html'

class PostView(DetailView):
    model = Post
    template_name = 'Task1/post.html'

class AddView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Task1/form.html'
    # fields = '__all__'

class EditView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "Task1/update.html"
    # fields = ['title', 'title_tag', 'content']

# class CascadeView(DeleteView):
#     model = Post
#     form_class = DeleteForm
#     template_name = ".html"

