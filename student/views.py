from django.shortcuts import render


def home(request):
    context={
    }
    return render(request, 'main_page/home.html', context)

def page_create_topic(request):
    context={
    }
    return render(request, 'main_page/page-create-topic.html', context)
