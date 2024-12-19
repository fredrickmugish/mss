from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # All registered pages
    path('', views.home, name='home'),
    path('word_from_headmaster/', views.word_from_headmaster, name='word_from_headmaster'),
    path('school_background/', views.school_background, name='school_background'),
    path('leadership/', views.leadership, name='leadership'),
    path('alumni/', views.alumni, name='alumni'),
    path('results/', views.results, name='results'),
    path('joining_instructions/', views.joining_instructions, name='joining_instructions'),
    path('school_facilities/', views.school_facilities, name='school_facilities'),
    path('school_gallery/', views.school_gallery, name='school_gallery'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),  # Added detail view
    path('contact/', views.contact, name='contact'),
    path('academic_results/', views.academic_results, name='academic_results'), 
 
  
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
