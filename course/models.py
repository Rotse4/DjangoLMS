from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

# Create your models here.


YEARS = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (4, "5"),
    (4, "6"),
)

SEMESTER = (
    ("FIRST", "First"),
    ("SECOND", "Second"),
    ("THIRD", "Third"),
)

class Course(models.Model):
    slug = models.SlugField(blank=True, unique=True)
    title = models.CharField(max_length=200, null=True)
    # book = models.FileField()
    # lessons = models.IntegerField()
    picture = models.ImageField(
        upload_to="course_pic/%y/%m/%d/", null=False
    )
    code = models.CharField(unique=True, max_length=200, null=True)
    credit=models.IntegerField(null=True, default=0)
    summary = models.TextField(max_length=200, blank=True, null=True)
    level = models.CharField(max_length=25) 
    year = models.IntegerField(choices=YEARS, default=0)
    semester = models.CharField(choices=SEMESTER, max_length=200)
    is_elective = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return "{0} ({1})".format(self.title, self.code, self.id)

# class Student(models.Model):
#     name = models.CharField(max_length=200)
#     book = models.FileField()
#     # lessons = models.IntegerField()





class Upload(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to="course_files/",
        help_text="Valid Files: pdf, docx, doc, xls, xlsx, ppt, pptx, zip, rar, 7zip",
        validators=[
            FileExtensionValidator(
                [
                    "pdf",
                    "docx",
                    "doc",
                    "xls",
                    "xlsx",
                    "ppt",
                    "pptx",
                    "zip",
                    "rar",
                    "7zip",
                ]
            )
        ],
    )
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    upload_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)



class CourseAllocation(models.Model):
    lecturer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="allocated_lecturer",
    )
    courses = models.ManyToManyField(Course, related_name="allocated_course")


    def __str__(self):
        return self.lecturer.get_full_name

