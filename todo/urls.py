from django.urls import path
from todo.views import ToDoCreateView, ToDoDetailView, ToDoListView, ToDoUpdateView, ToDoDeleteView

urlpatterns = [
    path('create/', ToDoCreateView.as_view(), name='create-todo'),
    path('<int:pk>/', ToDoDetailView.as_view(), name='retrieve-todo'),
    path('', ToDoListView.as_view(), name='list-todo'),
    path('update/<int:pk>/', ToDoUpdateView.as_view(), name='update-todo'),
    path('delete/<int:pk>/', ToDoDeleteView.as_view(), name='delete-todo'),
]
