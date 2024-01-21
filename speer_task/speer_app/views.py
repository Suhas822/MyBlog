# views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note, NoteShare
from .serializers import NoteSerializer
from django_ratelimit.decorators import ratelimit
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        # Check if the user is authenticated before saving the note
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            # Handle the case when the user is not authenticated
            # You can customize this part based on your requirements
            return Response({'detail': 'Authentication required to create a note'}, status=status.HTTP_401_UNAUTHORIZED)
class NoteDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    login_url = '/admin/login/'  # Specify your login URL here
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'

class NoteShareView(LoginRequiredMixin, generics.CreateAPIView):
    login_url = '/admin/login/'  # Specify your login URL here
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def post(self, request, *args, **kwargs):
        note = self.get_object()
        shared_with_username = request.data.get('shared_with_username')
        shared_with_user = get_object_or_404(User, username=shared_with_username)

        # Check if the note is owned by the current user
        if note.user == request.user:
            # Check if the note is already shared with the user
            if not NoteShare.objects.filter(note=note, shared_with=shared_with_user).exists():
                NoteShare.objects.create(note=note, shared_with=shared_with_user)
                return Response({'detail': 'Note shared successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Note is already shared with this user'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'You do not have permission to share this note'}, status=status.HTTP_403_FORBIDDEN)

class NoteSearchView(LoginRequiredMixin, generics.ListAPIView):
    login_url = '/admin/login/'  # Specify your login URL here
    serializer_class = NoteSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', '')
        return Note.objects.filter(content__icontains=q)
