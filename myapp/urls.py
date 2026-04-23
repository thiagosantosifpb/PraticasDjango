from django.contrib import admin
from django.urls import include, path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('edu.urls')),
    path('', views.home, name='home'),
    path('contato/<str:telefone>/', views.contato, name='contato'),
    path('blog/', include('blog.urls')),
]
