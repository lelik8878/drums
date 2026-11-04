
from django.urls import path
from .views import get_home_page, get_parts_page, get_history_page, get_account_page, get_add_page, get_total_page

urlpatterns = [
    path('', get_home_page, name='home'),
    path('parts/', get_parts_page, name='parts'),
    path('history/', get_history_page, name='history'),
    path('account/', get_account_page, name='account'),
    path('add/', get_add_page, name='add'),
    path('total/', get_total_page, name='total'),
]
