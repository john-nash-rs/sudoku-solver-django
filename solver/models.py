from django.db import models

class SudokuPuzzle(models.Model):
    puzzle = models.CharField(max_length=81)  # 9x9 grid serialized as a string
