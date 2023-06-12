from django.urls import path
from .views import article_list, article_create, article_update, article_detail, article_delete,index, accept, revize, reject


urlpatterns=[
    path('index/', index, name='index'),
    path('', article_list, name='article_list'),
    path('article_create/', article_create, name='article_create'),
    path('article_update/<slug>', article_update, name='article_update'),
    path('article_detail/<slug>', article_detail, name='article_detail'),
    path('article_delete/<slug>', article_delete, name='article_delete'),
    path('accept/', accept, name='accept'),
    path('revize/', revize, name='revize'),
    path('reject/', reject, name='reject'),
]

