from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def review_create(request):
    if request.method == "POST":
        Review.objects.create(
            title = request.POST['title'],
            year = request.POST['year'],
            category = request.POST['category'],
            rating = request.POST['rating'],
            runningTime = request.POST['runningTime'],
            review = request.POST['review'],
            director = request.POST['director'],
            actor = request.POST['actor']
        )
        return redirect('review:review_list')
    
    
    return render(request, 'review/create.html')

def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'review/list.html', context)

def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        'review': review
    }
    return render(request, 'review/detail.html', context)

def review_update(request, pk):
    review = Review.objects.get(id=pk)
    if request.method == "POST":
        review.title = request.POST['title']
        review.year = int(request.POST['year'])
        review.category = request.POST['category']
        review.rating = request.POST['rating']
        review.runningTime = request.POST['runningTime']
        review.review = request.POST['review']
        review.director = request.POST['director']
        review.actor = request.POST['actor']
        review.save()
        return redirect('review:review_detail', pk=review.pk)
    
    context = {
        'review': review
    }
    return render(request, 'review/update.html', context)

def review_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    
    return redirect('review:review_list')