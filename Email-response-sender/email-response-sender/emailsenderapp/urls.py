from django.contrib import admin
from django.urls import path
from emailsenderapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query',views.query,name='query')
]