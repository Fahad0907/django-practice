from rest_framework import pagination

class Mypage(pagination.LimitOffsetPagination):
    page_size = 100000