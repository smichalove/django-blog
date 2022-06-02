from pyexpat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from rest_framework import viewsets
from rest_framework import permissions

from blogging.models import Post, Category
from blogging.forms import MyPostForm
from blogging.serializers import PostSerializer, CategorySerializer





# Create your views here.
def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

# class BloggingListView(ListView):
#     # def as_view(self):
#     #     return self.get
#     model = Post
#     template_name = 'blogging/list.html'

#     def as_view(self):
#         return self.get

#     def list_view(self,request):
#         context = {'posts': Post.objects.all()}
#         return render(request, 'blogging/list.html', context)

#     def get(self,request):
#         model_list_name = self.model_name__.lower() + '_list'
#         context = {model_list_name: self.model.objects.all()}
#         return render(request, self.template_name, context)

class BlogListView(ListView):
    model = Post
    templat_name = 'blogging/list.html'
    # queryset = Post.objects.all()


    # def as_view(self):
    #     return self.get

    def list_view(self,request):
        
        context = {'posts': Post.objects.all()}
        return render(request, 'blogging/list.html', context)

    def get(self,request):
        model_list_name = self.model.__name__.lower() + '_list'
        context = {model_list_name: self.model.objects.all()}
        return render(request, 'blogging/list.html', context)



# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by("-published_date")
#     # template = loader.get_template('blogging/list.html')
#     context = {"posts": posts}
#     # body = template.render(context)
#     # return HttpResponse(body, content_type="text/html")
#     return render(request, "blogging/list.html", context)

class BloggingDetailView(DetailView):
    model = Post
    templat_name = 'blogging/detail.html'

    # def as_view(self):
    #     return self.get

    def get(self,request):
        model_list_name = self.model.__name__.lower() + '_list'
        context = {model_list_name: self.model.objects.all()}
        return render(request, self.template_name, context)




# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {"post": post}
#     return render(request, "blogging/detail.html", context)

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by("-published_date")
    context = {"posts": posts}
    return render(request, "blogging/list.html", context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {"post": post}
    return render(request, "blogging/detail.html", context)


def add_model(request):
    if request.method == "POST":
        form = MyPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect("/")
    else:
        form = MyPostForm()

        return render(request, "blogging/my_post_template.html", {"form": form})


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """

    queryset = Post.objects.all().order_by("-created_date")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
