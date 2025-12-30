from django import forms
from .models import Order  # ✅ import your model

class OrderForm(forms.ModelForm):
  class Meta:
    model = Order        # ✅ THIS LINE FIXES THE ERROR
    fields = [
  'first_name', 'last_name', 'email',
  'phone', 'address_line_1', 'address_line_2',
  'city', 'state', 'country', 'order_note'
]

