from django import forms
from .models import Books , Cateogry

class Add_book(forms.ModelForm):
    class Meta :
        model=Books
        fields="__all__"
        widgets = {
            'status' : forms.Select(attrs={'class' : 'form-control'}),
            'cateogry' : forms.Select(attrs={'class' : 'form-control'}),
            'rental_price_day ' : forms.NumberInput(attrs={'class' : 'form-control' , 'id':'rentalpriceday '}),
            'rental_period ' : forms.NumberInput(attrs={'class' : 'form-control' , 'id':'rentalperiod '}),
            'total_period ' : forms.NumberInput(attrs={'class' : 'form-control' , 'id':'totalperiod '}),
        }
        # exclude=("job",)

class Add_cateogry(forms.ModelForm):
    class Meta :
        model=Cateogry
        fields=['name']
        widgets = {
            'name' : forms.TimeInput(attrs={'class' : 'form-control'}),
        }

