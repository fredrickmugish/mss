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


# Model for Examination Results
class Result(models.Model):
    student_name = models.CharField(max_length=150, verbose_name="Student Name")
    student_id = models.CharField(max_length=50, unique=True, verbose_name="Student ID")
    subject = models.CharField(max_length=100, verbose_name="Subject")
    marks = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Marks")
    term = models.CharField(max_length=50, verbose_name="Term")
    year = models.IntegerField(verbose_name="Year")

    def __str__(self):
        return f"{self.student_name} - {self.subject} ({self.year})"


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


# Model for Student Results
class StudentResult(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=[('F', 'Female'), ('M', 'Male')], verbose_name="Sex")
    division = models.CharField(max_length=5, verbose_name="Division")
    points = models.IntegerField(verbose_name="Points")
    position = models.IntegerField(verbose_name="Position")
    detailed_subjects = models.TextField(verbose_name="Detailed Subjects")

    def __str__(self):
        return f"{self.name} - Division {self.division}"


# Model for Performance Overview
class PerformanceOverview(models.Model):
    sex = models.CharField(max_length=1, choices=[('F', 'Female'), ('M', 'Male'), ('T', 'Total')], verbose_name="Sex")
    division_i = models.IntegerField(default=0, verbose_name="Division I Count")
    division_ii = models.IntegerField(default=0, verbose_name="Division II Count")
    division_iii = models.IntegerField(default=0, verbose_name="Division III Count")
    division_iv = models.IntegerField(default=0, verbose_name="Division IV Count")
    division_0 = models.IntegerField(default=0, verbose_name="Division 0 Count")

    def __str__(self):
        return f"Performance Overview ({self.sex})"
