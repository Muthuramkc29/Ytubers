from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render
from .models import Youtuber
from django.db.models import FilteredRelation, Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers' : tubers
    }
    return render(request, 'youtubers/youtubers_home.html', data)


def youtuber_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber' : tuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)


def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    # Contains List of Distinct Cities
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    # Contains List of Distinct Camera_type
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    # Contains List of Distinct Category
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            # Does Description__icontains that particular keyword
            tubers = tubers.filter(Q(name__icontains=keyword)|Q(category__icontains=keyword))

    if 'city' in request.GET:
        tubers = Youtuber.objects.order_by('-created_date')
        city_name = request.GET['city']
        if city_name:
            tubers = tubers.filter(city__iexact=city_name)

    if 'camera_type' in request.GET:
        camera_name = request.GET['camera_type']
        if camera_name:
            tubers = Youtuber.objects.filter(camera_type__iexact=camera_name)

    if 'category' in request.GET:
        category_name = request.GET['category']
        if category_name:
            tubers = Youtuber.objects.filter(category__iexact=category_name)

    data = {
        'tubers' : tubers,
        'city_search' : city_search,
        'camera_type_search' : camera_type_search,
        'category_search' : category_search
    }
    return render(request, 'youtubers/search.html', data)

