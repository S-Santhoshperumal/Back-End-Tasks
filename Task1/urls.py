from django.urls import path
# from .import views
from .views import HomeView,PostView,AddView, EditView
urlpatterns = [
    # path('',views.home, name = 'home'),
    path('',HomeView.as_view(), name = 'home'),
    path('post/<int:pk>',PostView.as_view(), name = 'post-detail'),
    path("add-post/", AddView.as_view(), name="add-post"),
    path('post/edit/<int:pk>',EditView.as_view(), name = 'update-post')
]
