
from django.contrib import admin
from django.urls import path

# service_views와 views 추가

from . import views
from . import views as service_views

# from service.views import map, signup
# from service import views

app_name = 'service'

urlpatterns = [
    path("index", views.index),
    path("map", views.show_map),
    path("write", views.write),
    path("save", views.save),
    path("test", views.user_input_view),
    path("report",views.generate_report),

    path("admin/", admin.site.urls),
    # signup/ 을 map_system/templates/service/signup.html로 수정
    path("map/", service_views.map, name="map"),
    path("service/signup.html", service_views.signup, name="signup"),
    path('login/', views.login, name='login')
]