from django.shortcuts import render, redirect
from .models import Devtool
from .forms import DevtoolForm
from django.core.paginator import Paginator

# Create your views here.

def list(request):
    allDevtools = Devtool.objects.all()
    page = request.GET.get("page")
    paginator = Paginator(allDevtools, 8)
    devtools = paginator.get_page(page)
    context = {
        "devtools": devtools,
    }
    return render(request, "devtool/list.html", context)

def create(request):
    if request.method == "POST":
        form = DevtoolForm(request.POST)
        form.save()
        return redirect("devtool:devtool_list")
    
    form = DevtoolForm()
    
    context = {
        "form" : form,
    }
    
    return render(request, "devtool/create.html", context)

def detail(request, pk):
    devtool = Devtool.objects.get(id=pk)
    rel_ideas = devtool.idea_set.all()
    context = {
        "devtool": devtool,
        "rel_ideas": rel_ideas,
    }
    return render(request, "devtool/detail.html", context)

def delete(request, pk):
    if request.method == "POST":
        devtool = Devtool.objects.get(id=pk)
        devtool.delete()
        return redirect("devtool:devtool_list")
    return redirect("devtool:devtool_list")

def update(request, pk):
    devtool = Devtool.objects.get(id=pk)
    
    if request.method == "POST":
        form = DevtoolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
        return redirect("devtool:devtool_detail", devtool.id)
       
    form = DevtoolForm(instance=devtool)
    context = {
        "form": form,
        "devtool": devtool,
    }
    return render(request, "devtool/update.html", context)