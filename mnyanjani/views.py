import csv
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.contrib import messages
from .models import (
    ExamResult, SchoolPerformanceOverview, Facility, Alumni, GalleryItem, 
    News, JoiningInstruction, Headmaster, ContactMessage
)

def home(request):
    headmaster = Headmaster.objects.first()  # Assuming one headmaster
    latest_news = News.objects.order_by('-published_date')[:5]
    facilities = Facility.objects.all()[:3]
    gallery_items = GalleryItem.objects.order_by('-upload_date')[:5]
    return render(request, 'index.html', {
        'headmaster': headmaster,
        'latest_news': latest_news,
        'facilities': facilities,
        'gallery_items': gallery_items,
    })

def word_from_headmaster(request):
    return render(request, 'word_from_headmaster.html')

def school_background(request):
    return render(request, 'school_background.html')

def leadership(request):
    return render(request, 'leadership.html')

def alumni(request):
    alumni_list = Alumni.objects.order_by('-year_of_graduation')
    return render(request, 'alumni.html', {'alumni': alumni_list})

def results(request):
    all_results = Result.objects.order_by('-year', 'term')
    return render(request, 'results.html', {'results': all_results})

def joining_instructions(request):
    current_year = now().year
    instructions = JoiningInstruction.objects.all()
    return render(request, 'joining_instructions.html', {
        'instructions': instructions,
        'current_year': current_year,
    })

def school_facilities(request):
    all_facilities = Facility.objects.all()
    return render(request, 'school_facilities.html', {'all_facilities': all_facilities})

def school_gallery(request):
    gallery_items = GalleryItem.objects.order_by('-upload_date')
    return render(request, 'school_gallery.html', {'gallery_items': gallery_items})

def news_list(request):
    news_items = News.objects.order_by('-published_date')
    return render(request, 'news.html', {'news_items': news_items})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news_item': news_item})

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Thank you for reaching out. We will get back to you soon!")
        except Exception as e:
            messages.error(request, "An error occurred while sending your message. Please try again.")
    return render(request, 'contact.html')

    
def academic_results(request):
    # Get the selected class level from query parameters (default to 'Form 4')
    selected_class = request.GET.get('class', 'Form 4')

    # Fetch students' results for the selected class
    students = ExamResult.objects.filter(class_level=selected_class)

    # Calculate divisional performance overview for male and female students
    overview = {
        'male': {
            'division_i': students.filter(sex='M', division='I').count(),
            'division_ii': students.filter(sex='M', division='II').count(),
            'division_iii': students.filter(sex='M', division='III').count(),
            'division_iv': students.filter(sex='M', division='IV').count(),
            'division_0': students.filter(sex='M', division='0').count(),
        },
        'female': {
            'division_i': students.filter(sex='F', division='I').count(),
            'division_ii': students.filter(sex='F', division='II').count(),
            'division_iii': students.filter(sex='F', division='III').count(),
            'division_iv': students.filter(sex='F', division='IV').count(),
            'division_0': students.filter(sex='F', division='0').count(),
        }
    }

    # Render the results in the template
    return render(request, "academic_results.html", {
        "students": students,
        "overview": overview,
        "selected_class": selected_class,
    })
