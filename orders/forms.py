from django import forms


class OrderForm(forms.Form):
    dish_name = forms.CharField(label='Dish name', max_length=50)
    description = forms.CharField(label='Description', max_length=500)
    user = forms.IntegerField()