from django.db import models

# Create your models here.

class Parent(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class ClassDegrees(models.Model):
    number = models.IntegerField()
    subjects = models.ManyToManyField("Subject", related_name="subject_groups")

    class DegreeTypes(models.TextChoices):
        primary = "boshlang'ich", "Boshlang'ich"
        middle_school = "o'rta", "O'rta"
        high_school = "yuqori", "Yuqori"

    degree = models.CharField(
        choices = DegreeTypes.choices,
        default = DegreeTypes.primary,
        max_length = 120
    )

    def __str__(self):
        return f"{self.number}"

class Teacher(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class CreateClass(models.Model):
    letter_of_group = models.CharField(max_length=40)
    class_degree = models.ForeignKey(ClassDegrees, on_delete=models.SET_NULL, null=True)
    primary_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True, related_name="primary_teacher")

    def __str__(self):
        return f"{self.class_degree} - {self.letter_of_group}"

class Student(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    student_class = models.ForeignKey(CreateClass, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.name} - {self.status} - {self.parent}"
    
class Subject(models.Model):
    name = models.CharField(max_length=120)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="subject_teacher")
    def __str__(self):
        return self.name