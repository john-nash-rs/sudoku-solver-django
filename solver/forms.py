from django import forms
from .models import SudokuPuzzle

class SudokuForm(forms.ModelForm):
    class Meta:
        model = SudokuPuzzle
        fields = ['puzzle']
        widgets = {
            'puzzle': forms.TextInput(attrs={'class': 'sudoku-input', 'maxlength': 1}),
        }

# Create a list of 81 fields
SudokuForm.base_fields['puzzle'].widget = forms.TextInput(attrs={'class': 'sudoku-input', 'maxlength': 1})
SudokuForm.base_fields['puzzle'].label = ''
SudokuForm.base_fields['puzzle'].required = False
sudoku_fields = [SudokuForm(prefix=str(i)) for i in range(81)]
