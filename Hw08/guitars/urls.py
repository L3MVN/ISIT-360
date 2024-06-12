from django.urls import path

from . import views

urlpatterns = [
    # Empty (root) path goes to the index view
    path('', views.DepartmentListView.as_view(), name='index'),
    path("about", views.about, name="about"),
]