from django.urls import path
from . import views

urlpatterns = [
    path('run/', views.run_chess_game, name='run_chess_game'),
    # Add more URL patterns for your chess app as needed
]
