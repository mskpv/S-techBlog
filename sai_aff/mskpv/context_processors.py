from .models import Post, category, Comment, Reply

def get_search_list(request):
    category_search = category.objects.all()
    return {
        'category_search': category_search, 'host': '127.0.0.1:8000'
    }