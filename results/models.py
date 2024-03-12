from django.db import models
from django.core.validators import (
    MaxValueValidator,
    validate_comma_separated_integer_list,
)
from course.models import Course
from django.utils.translation import gettext_lazy as _

# Create your models here.

CATEGORY_OPTIONS = (
    ("assignment", _("Assignment")),
    ("exam", _("Exam")),
    ("practice", _("Practice Quiz")),
)

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null= True)
    title = models.CharField(verbose_name=_("Title"), max_length=60, blank=False)
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        help_text=_("A detailed description of the quiz"),
    )
    category = models.TextField(choices=CATEGORY_OPTIONS, blank=True)
    # pass_mark=models.SmallIntegerField(validators=[MaxValueValidator(100)])
    # correct_answer = models.


class Answer(models.Model):
    question = models.ForeignKey(Quiz, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
    