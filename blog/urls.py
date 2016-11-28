from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

from blog.models import Post

# The root of the blog app will be a LIST of all blog posts (well the first 25)
# Post.objects.all() returns all Post objects in a list
# You can then order these by the 'date' field, in REVERSE order (latest blog first)
# Use [:25] to only specify the most recent 25 posts.
urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by('-date')[:25],
                                template_name='blog/blog.html')),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
                                             template_name='blog/post.html'))
]

# The list passed to 'queryset' gets magically parsed into a Jinja variable called 'object_list'

# (?P) is a Django regex syntax to signify a NAMED group
# <pk> signifies the PRIMARY KEY for a table
# \d means 'digit', i.e. [0-9] - we only accept digits for this part of the url