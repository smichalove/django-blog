from django.forms import ModelForm
from blogging.models import Post
from blogging.models import Category
 
class MyPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']
       
class MyPostForm2(ModelForm):
    class Meta:
        model = Category
        fieild = ['name', 'description']
        exclude = ('primary',)