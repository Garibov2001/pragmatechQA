from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm

def home(request):
    context={
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

def post_create(request):
    form = QuestionForm(request.POST or None)
    wrong_tags = ''
    if request.method == "POST":
        if form.is_valid():
            # print(form.cleaned_data['tags'])
            # form.save()
            # print(Question.objects.last().tags.all())
            return redirect('student-home')
        else:
            wrong_tags = request.POST['tags']

    context={
        'form':form,
        'wrong_tags':wrong_tags
    }
    return render(request, 'main_page/post_create.html', context)

def user_details(request):
    return render(request, 'single-user/page-single-user.html')