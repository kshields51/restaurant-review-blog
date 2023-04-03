import os

from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

def individual_post_page(request, post_id):

    # get photo
    # find the right directory using post id

    # grab all images
    top_level_dir = "static/images"

    photos_filepaths = []
    for dir_name in os.listdir(top_level_dir):
        print(dir_name, post_id, "id is second")
        if dir_name == str(post_id) and os.path.isdir(os.path.join(top_level_dir, dir_name)):
            print(post_id, "post id")
            selected_dir = os.path.join(top_level_dir, dir_name)
            files = os.listdir(selected_dir)

            for photo in files:

                full_path = os.path.normpath(os.path.join(selected_dir, photo)) # normpath fixes a weird error where
                photos_filepaths.append(f"{post_id}/" + photo)

            break
        else:
            print("Directory 1 not found")

    print(photos_filepaths)

    # pass a list of those photos to the context
    latest_post = Post.objects.get(id=post_id)

    context = {'latest_post': latest_post, 'photos': photos_filepaths}
    print(latest_post.id)
    print(context)
    return render(request, 'restaurant_review/individual_post.html', context)

def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)

def display_all_posts(request):

    # select all from database

    # sort by date desc

    posts = Post.objects.order_by('-pub_date')
    context = {'all_posts': posts}

    return render(request, 'restaurant_review/index.html', context)


    # for post in posts

    # add them to a list

    # send the list as context
    pass

