from .models import Category

from django.db.models import Count


def menu_categories(request):
    cat_list = Category.objects.annotate(count=Count('article__id')).order_by('-count')[:6]

    return {'menu_categories': cat_list}