from django.http import JsonResponse
from student.models import *
from student.forms import QuestionForm, QuestionImageForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


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
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            new_question = form.save()  
            if((len(request.FILES) == 1) and (request.FILES['file[0]'].name == 'blob')):
                pass
            else:
                MAX_FILES = 2 # The number of max files (Client-Side 2)
                if (len(request.FILES) <= MAX_FILES ): 
                    for imageKey, imageValue in request.FILES.items():
                        questionData = {'question' : new_question}
                        imageData = {'image' : imageValue}
                        formImage = QuestionImageForm(questionData, imageData)
                        print('Burdan: ')
                        if(formImage.is_valid()):
                            formImage.save()
                        else:
                            return JsonResponse(formImage.errors.as_json(), safe = False)  
                else:
                    return JsonResponse(JsonResponse({'max_files' : 2}, safe = False))
                    
            return JsonResponse({'data' : 'form_valid'})
        else:
            return JsonResponse(form.errors.as_json(), safe = False)

    context={
        'form':form,
    }
    return render(request, 'main_page/post_create.html', context)

@login_required
def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    if request.method=="POST":
        if request.is_ajax():
            question=get_object_or_404(Question,id=request.POST.get("id"))
            stud=Student.objects.get(user=request.user)
            liked=question.action_set.filter(action_type=1).filter(student=stud).exists()
            disliked=question.action_set.filter(action_type=0).filter(student=stud).exists()
            if request.POST.get('type')=='question':
                if request.POST.get('action_type')=='dislike':
                    question.actions(0, stud, disliked, liked)
                else:
                    question.actions(1, stud, liked, disliked)
            return JsonResponse({'liked': str(liked), 'disliked': str(disliked)})
            

    else:
        question.view +=1
        question.save()
    context={
        'question': question,
        'student': Student.objects.first(),
    }
    return render(request, 'single-user/page-single-topic.html', context)
    
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