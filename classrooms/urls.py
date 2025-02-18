
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from Api_app.views import api_test, api_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', api_test, name="api-list"),
    path('test/detail/', api_detail, name="api-detail"),

    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),
    path('out/',views.no_access ,name='no-access'),

    path('classrooms/<int:classroom_id>/add/', views.student_add, name='student-add'),
    path('classrooms/<int:classroom_id>/students/<int:student_id>/update', views.student_update, name='student-update'),
    path('classrooms/<int:classroom_id>/students/<int:student_id>/delete', views.student_delete, name='student-delete'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
