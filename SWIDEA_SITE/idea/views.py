from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm
from django.core.paginator import Paginator

# Create your views here.
def main(request):
    return redirect('idea:idea_list')


def list(request):
    sort_value = request.GET.get('sort', 'id')
    
    page = request.GET.get("page")
    allIdeas = Idea.objects.all().order_by(sort_value)
    paginator = Paginator(allIdeas, 4)
    ideas = paginator.get_page(page)
    
    context = {
        'ideas' : ideas,
        'sort_value' : sort_value,
    }
    
    return render(request, 'idea/list.html', context)


def create(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("form is not valid")
        return redirect('idea:idea_list')
    
    form = IdeaForm()
    
    context = {
        "form": form,
    }
    
    return render(request, 'idea/create.html', context)
    

def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {
        'idea': idea,
    }
    return render(request, "idea/detail.html", context)

def update(request, pk):
    idea = Idea.objects.get(id=pk)
    
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea:idea_detail', idea.id)
    
    form = IdeaForm(instance=idea)
    context = {
        "idea": idea,
        "form": form,
    }
    return render(request, "idea/update.html", context)

def delete(request, pk):
    if request.method == 'POST':
        idea = Idea.objects.get(id=pk)
        idea.delete()
        return redirect('idea:idea_list')
    
    return redirect('idea:idea_list')
    
def zzimToggle(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.zzim = not idea.zzim
        idea.save()
        return JsonResponse({'zzim': idea.zzim})
    return JsonResponse({'error': "error"})

def interestup(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.interest += 1
        idea.save()
        return JsonResponse({'interest': idea.interest})
    return JsonResponse({'error': "error"})
def interestdown(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.interest -= 1
        idea.save()
        return JsonResponse({'interest': idea.interest})
    return JsonResponse({'error': "error"})