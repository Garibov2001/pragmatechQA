from django.shortcuts import render, redirect
from student.models import *
from student.forms import QuestionForm
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    form = QuestionForm(request.POST or None)
    wrong_tags = ''
    if request.method == "POST":
        if form.is_valid():
            print(dict(request.POST))
            print(dict(request.FILES))
            # new_question = form.save()

            # print(new_question)
            
            # imageDict = {}
            # for imageKey, imageValue in dict(request.FILES).items():
            #     imageDict['image'] = imageValue
            #     imageDict['question'] = new_question
            #     formImage = QuestionImageForm(imageDict) 
            #     if (formImage.is_valid()):
            #         print('Goood')
            #         formImage.save()
            #         # QuestionImage.objects.create(image = imageDict['image'], question = imageDict['question'])
            #     else:
            #         print('Question Image nese problem var qaqa.' )
                
            # post_item = form.save(commit=False)
            # post_item.save()
            # form.save()
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

def user_details(request, id):
    temp_student = User.objects.get(id = id).student
    context={
        'student' : temp_student,
        'questions' : temp_student.question_set.all(),
        'comments' : temp_student.comment_set.all(),
    }
    return render(request, 'single-user/page-single-user.html', context)