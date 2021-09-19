from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.utils import timezone
from ..models import Boards, Comment, Reply
from ..forms import BoardForm, CommentForm, ReplyForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login:login')
def comment_create(request, board_id):
    board = get_object_or_404(Boards, pk=board_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = request.user
            comment.create_date = timezone.now()
            comment.board = board
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('base:detail', board_id=board.id), comment.id))
    else:
        form = CommentForm()
    context = {'board': board, 'form': form}
    return render(request, 'base/board_detail.html', context)

@login_required(login_url='login:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user_id:
        messages.error(request, '수정권한이 없습니다')
        return redirect('base:detail', board_id=comment.board.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('base:detail', board_id=comment.board.id), comment.id))

    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'base/comment_form.html', context)

@login_required(login_url='login:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user_id:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('base:detail', board_id=comment.board.id)

@login_required(login_url='login:login')
def reply_create(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user_id = request.user
            reply.create_date = timezone.now()
            reply.board = comment.board
            reply.comment = comment
            reply.save()

            return redirect('{}#reply_{}'.format(
                resolve_url('base:detail', board_id=reply.board.id), reply.id))
    else:
        form = ReplyForm()
    context = {'form': form}
    return render(request, 'base/reply_form.html', context)

@login_required(login_url='login:login')
def reply_modify(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    if request.user != reply.user_id:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('base:detail', board_id=reply.board.id)

    if request.method == "POST":
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.modify_date = timezone.now()
            reply.save()
            return redirect('{}#reply_{}'.format(
                resolve_url('base:detail', board_id=reply.board.id), reply.id))
    else:
        form = ReplyForm(instance=reply)
    context = {'form': form}
    return render(request, 'base/comment_form.html', context)

@login_required(login_url='login:login')
def reply_delete(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    if request.user != reply.user_id:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('base:detail', board_id=reply.board.id)
    else:
        reply.delete()
    return redirect('base:detail', board_id=reply.board.id)