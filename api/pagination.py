from rest_framework.pagination import PageNumberPagination

class DishesPagination(PageNumberPagination):
    page_size = 4
    max_page_size = 100


class ReviewsPagination(PageNumberPagination):
    page_size = 8
    max_page_size = 100

class ReservationPagination(PageNumberPagination):
    page_size = 8
    max_page_size = 100

class TwelveItemsPagination(PageNumberPagination):
    page_size = 12
    max_page_size = 102