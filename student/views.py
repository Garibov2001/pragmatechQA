from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question


def home(request):

    question_list = Question.objects.all()

    paginator = Paginator(question_list, 5)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        
        questions = paginator.page(1)
    except EmptyPage:
        
        questions = paginator.page(paginator.num_pages)
    
    context={
        'questions':questions,
    }
    return render(request, 'main_page/home.html', context)

def tags(request):
    context={
    }
    return render(request, 'categories/tags.html', context)

def tag_info(request):
    context={
    }
    return render(request, 'categories/single_tag_info.html', context)

def about(request):
    return render(request, 'main_page/about.html')

def rules(request):
    return render(request, 'main_page/rules.html')

def page_create_topic(request):
    context={
    }
    return render(request, 'main_page/page-create-topic.html', context)

def user_details(request):
    return render(request, 'single-user/page-single-user.html')