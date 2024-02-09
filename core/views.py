from django.shortcuts import render,get_object_or_404, redirect
from django.views import View, generic
from core.models import *
from core.forms import *
from django.urls import reverse_lazy, reverse
# Create your views here.

class HomeView(View):
    def get(self, request):
        students_number = Student.objects.all().count()
        teachers_number = Teacher.objects.all().count()
        context = {
            "student_number" : students_number,
            "teachers_number" : teachers_number
        }
        return render(request, 'core/base.html', context)

class StudentsList(generic.ListView):
    model = Student
    template_name = "core/list.html"
    context_object_name = "students"
    queryset = Student.objects.all().order_by("-created_at")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['range'] = range(1, context['paginator'].num_pages + 1)
        context['accumulative'] =  context['paginator'].per_page * (context['page_obj'].number - 1)
        context['form'] = StudentForm()
        return context


class StudentUpdate(generic.UpdateView):
    model = Student
    template_name = "core/update.html"
    form_class = StudentForm
    success_url = reverse_lazy("students_list")

class ParentUpdate(generic.UpdateView):
    model = Parent
    template_name = "core/parent.html"
    form_class = ParentForm
    success_url = reverse_lazy("students_list")

class CreateStudent(generic.CreateView):
    model = Student
    template_name = "core/list.html"
    form_class = StudentForm
    success_url = reverse_lazy("students_list")

class DeleteStudent(View):
    def post(self, request, post_id):
        entered_student = get_object_or_404(Student, id=post_id)
        entered_student.delete()
        return redirect(reverse("students_list"))
    
class TeachersList(generic.ListView):
    model = Teacher
    template_name = "core/teachers.html"
    context_object_name = "teachers"
    queryset = Teacher.objects.order_by("-created_at")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        teacher = super().get_context_data(**kwargs)
        teacher['range'] = range(1, teacher['paginator'].num_pages + 1)
        teacher['form1'] = TeacherForm()
        teacher['form2'] = SubjectForm()
        return teacher

class TeacherUpdate(generic.UpdateView):
    model = Teacher
    template_name = "core/teacher_update.html"
    form_class = TeacherForm
    success_url = reverse_lazy("teachers_list")

class TeacherDelete(View):
    def post(self, request, teacher_id):
        entered_teacher = get_object_or_404(Teacher, id=teacher_id)
        entered_teacher.delete()
        return redirect(reverse("teachers_list"))
    
class CreateTeacher(generic.CreateView):
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy("teachers_list")


class CreateSubject(generic.CreateView):
    model = Subject
    form_class = SubjectForm
    success_url = reverse_lazy("teachers_list")

class StatisticsView(View):
    def get(self, request):
        students_number = Student.objects.all().count()
        teachers_number = Teacher.objects.all().count()
        parents_number = Parent.objects.all().count()
        classes_count = CreateClass.objects.all().count()
        subjects_count = Subject.objects.all().count()
        context = {
            "students_number" : students_number,
            "teachers_number" : teachers_number,
            "parents_number" : parents_number,
            "classes_count" : classes_count,
            "subjects_count" : subjects_count,
        }
        return render(request, "core/stats.html", context)
