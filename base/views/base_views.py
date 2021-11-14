from django.shortcuts import render, get_object_or_404
from ..models import Boards
from django.core.paginator import Paginator
from django.db.models import Q, Count


def index(request):
    page = request.GET.get('page', '1')
    cate = request.GET.get('cate', '전체')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    if cate == '자유':
        board_list = Boards.objects.all().filter(category = "1")
    elif cate == '정보':
        board_list = Boards.objects.all().filter(category = "2")
    elif cate == '질문':
        board_list = Boards.objects.all().filter(category = "3")
    else:  # all
        board_list = Boards.objects.all().order_by('-create_date')

    if kw:
        board_list = board_list.filter(
            Q(title__icontains = kw) |
            Q(content__icontains = kw) |
            Q(user_id__username__icontains = kw) |
            Q(comment__content__icontains = kw) |
            Q(comment__user_id__username__icontains = kw)
        ).distinct()

    board_list = board_list.annotate(
        num_voter = Count('voter', distinct = True),
        num_comment = Count('comment', distinct = True) + Count('reply', distinct = True) + Count('comment__reply',
                                                                                                  distinct = True))
    if so == 'recommend':
        board_list = board_list.order_by('-num_voter', '-create_date')
    elif so == 'popular':
        board_list = board_list.order_by('-num_comment', '-create_date')
    else:  # recent
        board_list = board_list.order_by('-create_date')

    paginator = Paginator(board_list, 13)
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj, 'cate': cate, 'page': page, 'kw': kw, 'so': so}

    return render(request, 'base/board_list.html', context)


def detail(request, board_id):
    board = get_object_or_404(Boards, pk = board_id)

    board.view_count += 1
    board.save()

    context = {'board': board}
    return render(request, 'base/board_detail.html', context)
