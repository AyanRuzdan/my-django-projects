"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import home_view
from q1.views import q1_view 
from q2.views import q2_view
from q3.views import q3_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('q1/post/<int:post_id>', q1_view),
    path('q2/book/<str:book_name>', q2_view),
    path('q3/student/<int:student_id>', q3_view),
]
