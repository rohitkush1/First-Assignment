from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('question_text')
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #template = loader.get_template('examination/index.html')
    context = {
        'latest_question_list' : latest_question_list #dictionary
    }

    return render(request, 'examination/index.html', context)


def detail(request, question_id):
    #return HttpResponse("You're looking at the Question %s." % question_id)
    question = get_object_or_404(Question, id = question_id)
    return render(request,'examination/detail.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'examination/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.clicks += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('examination:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'examination/results.html', {'question': question})

def instantvote(request):
    latest_question_list = Question.objects.order_by('question_text')
    context = {
                  'latest_question_list' : latest_question_list
     }

    return render(request, 'examination/instavote.html',context)



# Create your views here.
