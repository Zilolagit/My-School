from typing import Any
from core.models import *
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "name",
            "phone_number",
            "parent",
            "status",
            "student_class",
        ]
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != "status":
                self.fields[field].widget.attrs['class'] = "form-control mb-2"


class TeacherForm(forms.ModelForm):
    subject_teacher = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())
    primary_teacher = forms.ModelMultipleChoiceField(queryset=CreateClass.objects.all())
    class Meta:
        model = Teacher
        fields = [
            "name",
            "phone_number",
            "subject_teacher",
            "primary_teacher",
        ]
    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control mb-2"
    def save(self, commit=True):
        obj =  super().save(commit)
        obj.subject_teacher.set(self.cleaned_data['subject_teacher'])
        obj.primary_teacher.set(self.cleaned_data['primary_teacher'])
        return obj

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            "name",
            "teacher",
        ]
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control mb-2"
            

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = [
            "name",
            "phone_number",
        ]
    def __init__(self, *args, **kwargs):
        super(ParentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = "form-control mb-3"
        self.fields['phone_number'].widget.attrs['class'] = "form-control mb-3"