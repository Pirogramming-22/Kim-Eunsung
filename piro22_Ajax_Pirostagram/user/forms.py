from django import forms
from .models import User

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('id', 'password')
        widgets = {
            'password': forms.PasswordInput(),  # 비밀번호 필드에 비밀번호 입력 위젯 적용
        }

class LoginForm(forms.Form):
    id = forms.CharField(max_length=50, label="ID")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")