from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from ..models import Boards, Category
from ..forms import BoardForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='accounts:login')
def board_create(request):
    # 등록폼으로 처리
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user_id = request.user
            board.create_date = timezone.now()
            board.save()
            return redirect('base:index')
    # 게시글등록 버튼을 누를 경우
    else:
        form = BoardForm()

    context = {'form': form}
    return render(request, 'base/board_form.html', context)


@login_required(login_url='accounts:login')
def board_modify(request, board_id):
    board = get_object_or_404(Boards, pk=board_id)
    if request.user != board.user_id:
        messages.error(request, '수정권한이 없습니다')
        return redirect('base:detail', board_id=board.id)

    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.modify_date = timezone.now()
            board.save()
            return redirect('base:detail', board_id=board.id)
    else:
        form = BoardForm(instance=board)
    context = {'form': form}
    return render(request, 'base/board_form.html', context)

@login_required(login_url='accounts:login')
def board_delete(request, board_id):
    board = get_object_or_404(Boards, pk=board_id)
    if request.user != board.user_id:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('base:detail', board_id=board.id)
    board.delete()
    return redirect('base:index')