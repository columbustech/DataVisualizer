from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fetch_visualization/', fetch_visualization, name='fetch_visualization')
]
