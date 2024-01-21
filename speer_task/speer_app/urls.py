# urls.py
from django.urls import path
from .views import NoteListCreateView, NoteDetailView, NoteShareView, NoteSearchView

urlpatterns = [
    path('api/notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('api/notes/<int:id>/', NoteDetailView.as_view(), name='note-detail'),
    path('api/notes/<int:id>/share/', NoteShareView.as_view(), name='note-share'),
    path('api/search/', NoteSearchView.as_view(), name='note-search'),
]
