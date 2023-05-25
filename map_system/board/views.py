from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from board.models import Board
from board.forms import BoardForm

# Create your views here
class BoardList(ListView):  # 목록자료
    model = Board  # object_list로 전달


class BoardDetail(DetailView):  # 상세자료
    model = Board  # object로 전달!


def write(request):
    context = {"form": BoardForm(request.POST)}
    return render(request, "board/board_write.html", context)


def save(request):
    form = BoardForm(request.POST)
    board = form.save(commit=False)
    board.wdate = timezone.now()
    board.hit = 9
    board.save()

    return redirect("board:list")  # 화면에 list 띄워줌


# redirect -> 게시판 호출 못하고 이거 쓴느 이유; ㅈ미들웨어 거쳐와야,. 함수 직접 호출하지 않고
# redirect 해줘야
