
# Register your models here.

from django.contrib import admin
from .models import News, Facility, Alumni, Result, GalleryItem, ContactMessage,JoiningInstruction,Headmaster

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

# Registering the Result model
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_id', 'subject', 'marks', 'term', 'year')  # Fields to display in the admin list view
    search_fields = ('student_name', 'student_id', 'subject')  # Fields to search within
    list_filter = ('year', 'term')  # Filters by year and term

admin.site.register(Result, ResultAdmin)

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

