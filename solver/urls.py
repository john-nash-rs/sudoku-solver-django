from django.urls import path
from . import views

app_name = 'solver'

urlpatterns = [
    path('solve/', views.solve_sudoku, name='solve_sudoku'),
    # Add more URL patterns for other views as needed
]
