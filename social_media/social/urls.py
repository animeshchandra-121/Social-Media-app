from django.urls import path, include
from . import views

app_name = 'social' 
urlpatterns = [
    path('post/', views.post_list, name='post'),
    path('posts/<int:id>/', views.postdetailview, name='post-detail'),
    path('update-post/<int:id>/', views.update_post, name='update-post'),
    path('delete-post/<int:id>/', views.delete_post, name='delete-post'),
    path('profile/<int:id>/', views.profile_view, name= "profile"),
    path("profile/update-profile/<int:id>/", views.edit_profile, name="update-profile"),
    path("profile/<int:id>/add-follower/", views.addFollower, name="add-follower"),
    path("profile/<int:id>/remove-follower/", views.removeFollower, name="remove-follower"),
    path("post/<int:id>/likes", views.addlikes, name="add-likes"),
    path("post/<int:id>/dislikes", views.removelikes, name="remove-likes"),
    path("search/", views.search_bar, name='search')
]