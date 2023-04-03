from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_all_posts, name='index'),

    # ex: /food-blog/5/
    path('<int:post_id>/', views.individual_post_page, name='individual_post_page'),
]
