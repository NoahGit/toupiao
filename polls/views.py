# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:6]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class UserLoginView(generic.DetailView):
    template_name = 'polls/userLogin.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def ulogin(request):
    return render(request, 'polls/userLogin.html')


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'polls/welcome.html', {'username': user_name})
            else:
                return render(request, 'polls/userLogin.html')
        else:
            return render(request, 'polls/userLogin.html')
    elif request.method == 'GET':
        return render(request, 'polls/userLogin.html')

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message':"You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
