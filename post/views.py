from django.shortcuts import render, HttpResponse
from post.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests


def post_search(request):
    photos = None
    error = None

    # Get arguments
    query_title = request.GET.get('title')
    page = request.GET.get('page')

    if query_title:
        # Store the keyword in database
        post, created = Post.objects.get_or_create(title=query_title)
        post.hits += 1
        post.save()

        try:
            result = post.search_title_with_api()
            photo_list = result['photos']['photo']
            # Generate pagination object
            paginator = Paginator(photo_list, 6)

            try:
                photos = paginator.page(page)

            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                photos = paginator.page(1)

            except EmptyPage:
                # If page is out of range (e.g 99999), deliver last page of results.
                photos = paginator.page(paginator.num_pages)

        # If there is no internet connection, we will catch the error.
        except requests.ConnectionError as e:
            error = "There Is No Internet Connection"
            print("Exception: {}, message: {}".format(e, error))

    # Fetch previous searches sorted by date from the database.
    previous_search = Post.objects.order_by('-search_time').all()[:20]

    # Variables are passed in json.
    context = {
        'photos': photos,
        'previous_search': previous_search,
        'title': query_title,
        'error': error
    }

    return render(request, 'index.html', context)
