from django.shortcuts import render, redirect
from student.models import *
from student.forms import QuestionForm
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from taggit.models import Tag


def home(request):

    question_list = Question.objects.all().order_by('-updated')

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
    template = 'categories/tags.html' 
    page_template = 'categories/tag-list.html'
    context={
        'tags' : Tag.objects.all().order_by('name') if Tag.objects.all() else -1,
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)

def tag_info(request, slug):
    template = 'categories/single-tag.html' 
    page_template = 'categories/single-tag-questions.html'
    tag = Tag.objects.filter(slug = slug).first()
    questions = Question.objects.filter(tags__in = [tag])
    context={
        "tag" : tag,
        "questions" : questions,
        "page_template": page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, 'categories/single-tag.html', context)

def about(request):
    return render(request, 'main_page/about.html')

def rules(request):
    return render(request, 'main_page/rules.html')

def page_create_topic(request):
    form = QuestionForm(request.POST or None)
    wrong_tags = ''
    if request.method == "POST":
        if form.is_valid():
            # post_item = form.save(commit=False)
            # post_item.save()
            form.save()
            return redirect('student-home')
        else:
            wrong_tags = request.POST['tags']

    context={
        'form':form,
        'wrong_tags':wrong_tags
    }
    return render(request, 'main_page/post_create.html', context)

def faq(request):
    context={
    }
    return render(request, 'main_page/page-tabs.html', context)

def user_activity(request, id):
    template='user-details/user-activity.html' 
    page_template='user-details/user-activity-list.html'
    temp_student = User.objects.get(id = id).student
    context={
        'student' : temp_student,
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)

def user_questions(request, id):
    template='user-details/user-questions.html'
    page_template='user-details/user-question-list.html'
    temp_student = User.objects.get(id = id).student
    context={
        'student' : temp_student,
        'questions' : temp_student.question_set.all().order_by('-updated') if temp_student.question_set.all() else -1,
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)

def user_comments(request, id):
    template = 'user-details/user-comments.html'
    page_template = 'user-details/user-comment-list.html'
    temp_student = User.objects.get(id = id).student
    context={
        'student' : temp_student,
        'comments' : temp_student.comment_set.all().order_by('-updated') if temp_student.comment_set.all() else -1,
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)

def user_tags(request, id):
    template = 'user-details/user-tags.html' 
    page_template = 'user-details/user-tag-list.html'
    temp_student = User.objects.get(id = id).student
    my_tags = set()
    for question in temp_student.question_set.all():
        for tag in question.tags.all():
            my_tags.add(tag)
    custom_list = [tag.id for tag in my_tags]
    context={
        'student' : temp_student,
        'tags' : Tag.objects.filter(id__in=custom_list).order_by('name') if Tag.objects.filter(id__in=custom_list) else -1,
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)