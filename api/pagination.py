from rest_framework.pagination import PageNumberPagination

class DishesPagination(PageNumberPagination):
    page_size = 4  # Taille de page fixe : 10 éléments
    max_page_size = 100  # Limite maximale en cas d’extension future


class ReviewsPagination(PageNumberPagination):
    page_size = 8  # Taille de page fixe : 10 éléments
    max_page_size = 100  # Limite maximale en cas d’extension future

class ReservationPagination(PageNumberPagination):
    page_size = 8  # Taille de page fixe : 10 éléments
    max_page_size = 100  # Limite maximale en cas d’extension future

class TwelveItemsPagination(PageNumberPagination):
    page_size = 12  # Taille de page fixe : 12 éléments
    max_page_size = 102