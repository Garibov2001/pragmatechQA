from django.shortcuts import render

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

def staff_and_users(request):
    return render(request, 'categories/single_tag_info.html')

