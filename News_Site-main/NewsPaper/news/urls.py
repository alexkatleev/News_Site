from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, NewsCreate, PostUpdate, PostDelete, PostSearch, CategoryListView
from .filters import *
from .views import upgrade_me, subscribe


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_filter'),
   path('create/news', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'), 
   path('upgrade/', upgrade_me, name = 'upgrade'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'), 
]