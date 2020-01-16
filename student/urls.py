from django.urls import path
from . import views

urlpatterns = [
    path('class-wise-student-registration', views.class_wise_student_registration, name='class-wise-student-registration'),
    path('student-registration', views.student_registration, name='student-registration'),
    path('student-list', views.student_list, name='student-list'),
    path('profile/<student_id>', views.student_profile, name='student-profile'),
    path('edit/<student_id>', views.student_edit, name='student-edit'),
    path('delete/<student_id>', views.student_delete, name='student-delete'),
    path('student-search/', views.student_search, name='student-search'),
]
