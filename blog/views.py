from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def blog_page(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'blog/blog.html'
    )

def exemplo(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'blog/exemplo.html'
    )