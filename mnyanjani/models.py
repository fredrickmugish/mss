from django.db import models

# Model for the School News
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="News Title")
    content = models.TextField(verbose_name="News Content")
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="News Image")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Published Date")

    def __str__(self):
        return self.title


# Model for School Facilities
class Facility(models.Model):
    name = models.CharField(max_length=100, verbose_name="Facility Name")
    description = models.TextField(verbose_name="Facility Description")
    image = models.ImageField(upload_to='facilities/', blank=True, null=True, verbose_name="Facility Image")

    def __str__(self):
        return self.name


# Model for Alumni
class Alumni(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Full Name")
    year_of_graduation = models.IntegerField(verbose_name="Year of Graduation")
    current_position = models.CharField(max_length=200, blank=True, null=True, verbose_name="Current Position")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(upload_to='alumni/', blank=True, null=True, verbose_name="Alumni Photo")

    def __str__(self):
        return self.full_name


# Model for Gallery
class GalleryItem(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(upload_to='gallery/', verbose_name="Image")
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name="Upload Date")

    def __str__(self):
        return self.title


# Model for Contact Messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=150, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Sent At")

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


# Model for Joining Instruction
class JoiningInstruction(models.Model):
    year = models.IntegerField(verbose_name="Year")
    file = models.FileField(upload_to='joining_instructions/', verbose_name="Joining Instruction File")
    title = models.TextField(blank=True, null=True, verbose_name="Title")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded At")

    def __str__(self):
        return f"Joining Instruction for {self.year}"


# Model for the Headmaster
class Headmaster(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default="School Headmaster")
    image = models.ImageField(upload_to='headmaster_photos/')
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ExamResult(models.Model):
    CLASS_LEVEL_CHOICES = [
        ('Form 1', 'Form 1'),
        ('Form 2', 'Form 2'),
        ('Form 3', 'Form 3'),
        ('Form 4', 'Form 4'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    DIVISION_CHOICES = [
        ('I', 'Division I'),
        ('II', 'Division II'),
        ('III', 'Division III'),
        ('IV', 'Division IV'),
        ('0', 'Division 0'),
    ]

    name = models.CharField(max_length=100, verbose_name="Student Name")
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Sex")
    division = models.CharField(max_length=3, choices=DIVISION_CHOICES, verbose_name="Division")
    points = models.PositiveIntegerField(verbose_name="Points")
    position = models.PositiveIntegerField(verbose_name="Position")
    detailed_subjects = models.TextField(verbose_name="Detailed Subjects")
    class_level = models.CharField(max_length=10, choices=CLASS_LEVEL_CHOICES, verbose_name="Class Level",null=True)

   
    def __str__(self):
        return f"{self.name} - {self.class_level} - Division {self.division}"


    class Meta:
        verbose_name = "Exam Result"
        verbose_name_plural = "Exam Results"


class SchoolPerformanceOverview(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Total'),
    ]

    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Sex")
    division_i = models.PositiveIntegerField(verbose_name="Division I")
    division_ii = models.PositiveIntegerField(verbose_name="Division II")
    division_iii = models.PositiveIntegerField(verbose_name="Division III")
    division_iv = models.PositiveIntegerField(verbose_name="Division IV")
    division_0 = models.PositiveIntegerField(verbose_name="Division 0")

    def __str__(self):
        return f"{self.get_sex_display()} Performance"

    class Meta:
        verbose_name = "School Performance Overview"
        verbose_name_plural = "School Performance Overviews"