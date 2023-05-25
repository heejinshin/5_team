from django.contrib import admin
from django.urls import path


from . import views
from board.views import BoardList, BoardDetail

# namespace 생성

# redirect(app_name: path의 name속성)
app_name = "board"
urlpatterns = [
    path("list", BoardList.as_view(), name="list"),
    path("detail/<int:pk>", BoardDetail.as_view()),
    # board_detail.html
    path("write/", views.write),
    path("save/", views.save),
]
