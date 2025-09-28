from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        """
        Vote for a choice on a question.
        """
        question = self.get_object()
        try:
            choice_id = request.data['choice']
            selected_choice = question.choice_set.get(pk=choice_id)
        except (KeyError, Choice.DoesNotExist):
            return Response({'error': 'Invalid choice.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return Response(QuestionSerializer(question).data)

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows choices to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

