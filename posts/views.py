from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, ListView

from posts.models import Blogpost, Bannerpost, Categories


class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


class HomeView(TemplateView):
    template_name = "home.html"
    model = Blogpost
    paginate_by = 6
    paginator_class = MyPaginator  # We use our paginator class

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = Bannerpost.objects.order_by('-date_added')[:1]
        # context['post'] = Blogpost.objects.all()
        context['categories'] = Categories.objects.all()
        page = self.request.GET.get('page', 1)
        post = Blogpost.objects.all().order_by('-updated_on')
        paginator = self.paginator_class(post, self.paginate_by)
        post = paginator.page(page)
        context['post'] = post

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['post'] = context['post'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context


def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        categories = Categories.objects.get(category_name=categoryFromForm)
        # all views:
        banner = Bannerpost.objects.order_by('-date_added')[:1]
        post = Blogpost.objects.filter(category=categories)
        allCategories = Categories.objects.all()
        return render(request, "home.html", {
            "banner": banner,
            "post": post,
            "categories": allCategories
        })


class BlogDetailView(DetailView):  # new
    template_name = 'blog_detail.html'
    model = Blogpost
    request_user = Blogpost.author


class BlogCreateView(LoginRequiredMixin, CreateView):  # new
    model = Blogpost
    template_name = 'blog_new.html'
    user = Blogpost.author
    fields = ['title', 'summary', 'imageUrl', 'imageCaption', 'description', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):  # new
    model = Blogpost
    template_name = 'blog_edit.html'
    fields = ['title', 'summary', 'imageUrl', 'imageCaption', 'description', 'category']

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied()
        return super().post(request, *args, **kwargs)


class BlogDeleteView(LoginRequiredMixin, DeleteView):  # new
    model = Blogpost
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            raise Http404
        return super().post(request, *args, **kwargs)


class CatListView(ListView):
    template_name = 'catlist.html'
    queryset = Categories.objects.all()


def category_posts(request, category_id):
    category = Categories.objects.get(id=category_id)
    posts = Blogpost.objects.filter(category=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'category.html', context)


