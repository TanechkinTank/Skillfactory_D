from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostEdit, PostDelete


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:id>', PostDetail.as_view()),
   path('search/', PostSearch.as_view()),
   path('create/', PostCreate.as_view()),
   path('<int:pk>/edit/', PostEdit.as_view()),
   path('<int:pk>/delete/', PostDelete.as_view()),

]