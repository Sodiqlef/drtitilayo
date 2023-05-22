from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Journal, BookCount


def paging(val, queryset, request):
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, val)
    try:
        journals = paginator.page(page)
    except PageNotAnInteger:

        journals = paginator.page(1)
    except EmptyPage:
        journals = paginator.page(paginator.num_pages)

    return journals

# Create your views here.


def index(req):
    liveCount = BookCount.objects.first()
    return render(req, 'index.html', {'liveCount': liveCount})


def books(req):
    return render(req, 'books.html')


def donate(req):
    return render(req, 'donate.html')


def establishment(req):
    return render(req, 'establishment.html')


def journal(req):
    queryset = Journal.objects.all().order_by('-created_at')
    journals = paging(1, queryset, req)
    return render(req, 'journal.html', {'journals': journals})


def journal_detail(req, pk):
    journal = get_object_or_404(Journal, pk=pk)
    return render(req, 'journal_detail.html', {'journal': journal})


def se(req):
    return render(req, 'se.html')


def testimonial(req):
    return render(req, 'testimonial.html')
