"""B9_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("viewa-a/", views.view_a, name="view_a"),

    # library urls
    path('book/', include('app.urls')), #new

    # user app urls
    path('user/', include('user_app.urls')), #new

    # path('cbv/', include('cbv_app.urls')) #class based


]

# patterns/url patterns/urls/endpoints -- 
# http://127.0.0.1:8000/book/admin/
# http://127.0.0.1:8000/book/home/
# http://127.0.0.1:8000/book/show-books/
# http://127.0.0.1:8000/book/show-single-book/1/
# http://127.0.0.1:8000/book/add-book/
# http://127.0.0.1:8000/book/edit-book/1/
# http://127.0.0.1:8000/book/delete-book/1/
# http://127.0.0.1:8000/book/soft-delete-book/1/
# http://127.0.0.1:8000/book/form-view/


# user_app urls
# http://127.0.0.1:8000/user/signup/


# cbv_app
# http://127.0.0.1:8000/cbv/new-cview

