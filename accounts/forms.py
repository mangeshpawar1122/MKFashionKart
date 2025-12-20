from django import forms
from .models import Account


class RegistrationForms(forms.ModelForm):
  password = forms.CharField(
    widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter a password',
        'class': 'form-control'
    })
)

  confirm_password = forms.CharField(
    widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm a password',
       # 'class': 'form-control'
    })
)

  class Meta:
    model = Account
    fields =['first_name','last_name','phone_number','email','password']

  
  def clean(self):
     clean_data=super(RegistrationForms,self).clean()
     password=clean_data.get('password')
     confirm_password=clean_data.get('confirm_password')

     if password != confirm_password:
        raise forms.ValidationError("Password does not mach!")
         
  
  def __init__(self,*args,**kwargs):
    super(RegistrationForms,self).__init__(*args,**kwargs)
    self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
    self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
    self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
    self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
    for field in self.fields:
        self.fields[field].widget.attrs['class'] = 'form-control'
 