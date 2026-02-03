from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from books.models import Book
from reviews.forms import ReviewCreateForm, ReviewEditForm, ReviewDeleteForm
from reviews.models import Review


def recent_reviews(request: HttpRequest) -> HttpResponse:
    DEFAULT_REVIEWS_COUNT = 5
    reviews_count = int(request.GET.get('count', DEFAULT_REVIEWS_COUNT))

    reviews = Review.objects.select_related('book')[:reviews_count]

    context = {
        'reviews': reviews,
        'page_title': 'Recent reviews',
    }

    return render(request, 'reviews/list.html', context)


def review_details(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )

    context = {
        'review': review,
        'page_title': f'{review.author}\'s review on {review.book.title}',
    }

    return render(request, 'reviews/details.html', context)


def review_create(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            # Redirect към детайлите на книгата с slug
            return redirect('books:details', slug=book.slug)
    else:
        form = ReviewCreateForm()

    return render(request, 'books/list.html', {'form': form, 'book': book})


def review_edit(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    form = ReviewEditForm(request.POST or None, instance=review)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('reviews:list') # Redirect to the reviews list after edit

    context = {
        "form": form,
    }

    return render(request, 'reviews/edit.html', context)


def review_delete(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    form = ReviewDeleteForm(request.POST or None, instance=review)

    if request.method == "POST" and form.is_valid():
        review.delete()
        return redirect('reviews:list') # Redirect to the reviews list after deletion

    context = {
        "form": form,
    }

    return render(request, 'reviews/delete.html', context)