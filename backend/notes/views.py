from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def note_list(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def note_detail(request, id):
    note = get_object_or_404(Note, id=id)
    serializer = NoteSerializer(note)
    return Response(serializer.data)

# Create your views here.
