from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Boards


@login_required(login_url='accounts:login')
def vote_board(request, board_id):
    board = get_object_or_404(Boards, pk=board_id)
    if request.user == board.user_id:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        board.voter.add(request.user)
    return redirect('base:detail', board_id=board.id)