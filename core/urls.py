from django.urls import path
from core.views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home_view"),
    path('students/', StudentsList.as_view(), name="students_list"),
    path('student/<int:pk>/', StudentUpdate.as_view(), name="student_update"),
    path('parent/<int:pk>/', ParentUpdate.as_view(), name="parent_update"),
    path('students/add/', CreateStudent.as_view(), name="new_student_add"),
    path('student/<int:post_id>/delete/', DeleteStudent.as_view(), name="student_delete"),
    path("teachers/", TeachersList.as_view(), name="teachers_list"),
    path("teacher/<int:pk>/", TeacherUpdate.as_view(), name="teacher_update"),
    path("teacher/<int:teacher_id>/delete/", TeacherDelete.as_view(), name="teacher_delete"),
    path("teacher/add/", CreateTeacher.as_view(), name="new_teacher_add"),
    path("subject/add/", CreateSubject.as_view(), name="new_subject_add"),
    path("stats/", StatisticsView.as_view(), name="stats"),
]