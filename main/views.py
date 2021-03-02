from django.views import generic
from .models import Question, Choice

class PollsListView(generic.ListView):
    model = Question
    template_name = 'main/polls_list.html'
