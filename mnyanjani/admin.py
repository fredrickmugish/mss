
# Register your models here.

from django.contrib import admin
from .models import News, Facility, Alumni, GalleryItem, ContactMessage,JoiningInstruction,Headmaster, ExamResult, SchoolPerformanceOverview
from django.contrib import admin
from django import forms
import csv
import io

class ExamResultAdminForm(forms.ModelForm):
    
    upload_file = forms.FileField(
        required=False, 
        help_text="Upload an Excel or CSV file to add multiple exam results at once."
    )

    class Meta:
        model = ExamResult
        fields = '__all__'

class ExamResultAdmin(admin.ModelAdmin):
    form = ExamResultAdminForm

    list_display = ('name', 'sex', 'division', 'points', 'position', 'detailed_subjects')
    list_filter = ('class_level',)
    def get_queryset(self, request):
     
        queryset = super().get_queryset(request)

        if 'class_level__exact' not in request.GET:

            queryset = queryset.filter(class_level="Form 4")

        return queryset
    def save_model(self, request, obj, form, change):
    
        super().save_model(request, obj, form, change)

     
        upload_file = form.cleaned_data.get("upload_file")
        if upload_file:
          
            data = upload_file.read().decode('utf-8')
            csv_reader = csv.reader(io.StringIO(data))
            next(csv_reader)  

            for row in csv_reader:
                name, sex, division, points, position, detailed_subjects = row
                ExamResult.objects.create(
                    name=name,
                    sex=sex,
                    division=division,
                    points=int(points),
                    position=int(position),
                    detailed_subjects=detailed_subjects,
                )

            self.message_user(request, "Exam results uploaded successfully!")

admin.site.register(ExamResult, ExamResultAdmin)



# Registering the News model
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')  # Fields to display in the admin list view
    search_fields = ('title', 'content')       # Fields to search within
    list_filter = ('published_date',)          # Filter by publication date

admin.site.register(News, NewsAdmin)

# Registering the Facility model
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Fields to display in the admin list view
    search_fields = ('name', 'description')  # Fields to search within

admin.site.register(Facility, FacilityAdmin)

# Registering the Alumni model
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'year_of_graduation')  # Fields to display in the admin list view
    search_fields = ('full_name', 'current_position', 'description')  # Fields to search within

admin.site.register(Alumni, AlumniAdmin)


# Registering the GalleryItem model
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')  # Fields to display in the admin list view
    search_fields = ('title', 'description')  # Fields to search within

admin.site.register(GalleryItem, GalleryItemAdmin)

# Registering the ContactMessage model
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'sent_at')  # Fields to display in the admin list view
    search_fields = ('name', 'email','message')  # Fields to search within

admin.site.register(ContactMessage, ContactMessageAdmin)


    # Registering the JoiningInstruction model
class JoiningInstructionAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'uploaded_at')  # Fields to display in the admin list view
    search_fields = ('title', 'year')  # Fields to search within
    list_filter = ('year',)  # Adds a filter sidebar for the 'year' field

# Register the model with the admin site
admin.site.register(JoiningInstruction, JoiningInstructionAdmin)


# Registering the Headmaster model
class HeadmasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')  # Fields to display in the admin list view
    search_fields = ('name', 'title')  # Fields to search within

admin.site.register(Headmaster, HeadmasterAdmin)




# Customize the admin site
admin.site.site_header = "MNYANJANI SECONDARY ADMIN"  # Appears at the top of the admin panel
admin.site.site_title = "mnyanjani secondary school"      # Appears in the browser tab title
admin.site.index_title = "Welcome to Mnyanjani Sec School Admin"  # Appears on the admin home page

