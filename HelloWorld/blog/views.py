from django.shortcuts import render_to_response

# Create your views here.

from blog.models import BlogPost

def archive(request):
	posts=BlogPost.objects.all()
	return render_to_response('archive.html',{'posts':posts})